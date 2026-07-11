from __future__ import annotations

import argparse
import csv
from collections import defaultdict
from pathlib import Path
import sys

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.evaluate_corruptions import corrupt_records, load_feature_cache_if_present
from scripts.generate_benchmark_grid import MVTEC_CLASSES, VISA_CLASSES
from src.backbones.dinov2 import build_backbone
from src.calibration.gated import ShiftGateSummary, anchored_gated_probabilities, gated_probabilities, no_harm_gate_strength, noise_safe_soft_gate, structured_shift_gate
from src.calibration.platt import VectorPlattScaler, entropy_binary
from src.config import load_config
from src.conformal import DensityRatioLogistic, effective_sample_size, pca_patch_covariates
from src.data.datasets import load_records
from src.data.sampling import evaluation_records, few_shot_support
from src.evaluation.metrics import ece_binary, summarize_binary
from src.models.baselines import build_model
from src.run_experiment import encode_with_cache

EXPERTS = ["vector_platt", "shift_aware_vector_platt", "weighted_platt"]


def write_csv(path: Path, rows: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not rows:
        path.write_text("", encoding="utf-8")
        return
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def read_existing(path: Path) -> list[dict]:
    if not path.exists() or path.stat().st_size == 0:
        return []
    with path.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def summarize(rows: list[dict], group_keys: list[str], metrics: list[str]) -> list[dict]:
    groups: dict[tuple, list[dict]] = defaultdict(list)
    for row in rows:
        groups[tuple(row[key] for key in group_keys)].append(row)
    out = []
    for key, group in sorted(groups.items(), key=lambda item: tuple(str(v) for v in item[0])):
        item = {group_key: value for group_key, value in zip(group_keys, key)}
        item["n"] = len(group)
        for metric in metrics:
            vals = []
            for row in group:
                try:
                    value = float(row[metric])
                except (KeyError, ValueError):
                    continue
                if np.isfinite(value):
                    vals.append(value)
            item[f"{metric}_mean"] = float(np.mean(vals)) if vals else float("nan")
            item[f"{metric}_std"] = float(np.std(vals, ddof=1)) if len(vals) > 1 else 0.0
        out.append(item)
    return out


def delta_rows(summary_rows: list[dict]) -> list[dict]:
    by_key: dict[tuple, dict[str, dict]] = defaultdict(dict)
    for row in summary_rows:
        key = (row["dataset"], row["corruption"], row["k_shot"])
        by_key[key][row["method"]] = row
    out = []
    for (dataset, corruption, k), methods in sorted(by_key.items(), key=lambda item: tuple(str(v) for v in item[0])):
        if "vector_platt" not in methods:
            continue
        base = methods["vector_platt"]
        for method, row in sorted(methods.items()):
            if method == "vector_platt":
                continue
            item = {"dataset": dataset, "corruption": corruption, "k_shot": k, "method": method, "n": row["n"]}
            for metric in ["auroc", "ap", "ece", "brier", "nll", "entropy_mean"]:
                b = float(base[f"{metric}_mean"])
                v = float(row[f"{metric}_mean"])
                item[f"vector_{metric}"] = b
                item[f"method_{metric}"] = v
                item[f"delta_{metric}_minus_vector"] = v - b
            item["no_harm_ece_vs_vector"] = float(item["delta_ece_minus_vector"] <= 0.01)
            out.append(item)
    return out


def oracle_gap_rows(summary_rows: list[dict]) -> list[dict]:
    by_key: dict[tuple, dict[str, dict]] = defaultdict(dict)
    for row in summary_rows:
        key = (row["dataset"], row["corruption"], row["k_shot"])
        by_key[key][row["method"]] = row
    out = []
    for (dataset, corruption, k), methods in sorted(by_key.items(), key=lambda item: tuple(str(v) for v in item[0])):
        if "oracle_best" not in methods:
            continue
        oracle = float(methods["oracle_best"]["ece_mean"])
        for method in ["vector_platt", "shift_aware_vector_platt", "weighted_platt", "structured_rule_gate", "soft_neff_gate", "anchored_structured_gate", "anchored_soft_gate", "anchored_structured_gate_adaptive", "anchored_soft_gate_adaptive"]:
            if method in methods:
                out.append(
                    {
                        "dataset": dataset,
                        "corruption": corruption,
                        "k_shot": k,
                        "method": method,
                        "ece_mean": float(methods[method]["ece_mean"]),
                        "oracle_ece_mean": oracle,
                        "oracle_gap_ece": float(methods[method]["ece_mean"]) - oracle,
                    }
                )
    return out


def get_features(config: dict, records: list, cache_name: str, seed: int, cache_seed: int | None = None):
    backbone_cfg = config.get("backbone", {})
    experiment_cfg = config.get("experiment", {})
    dataset_cfg = config.get("dataset", {})
    backbone_name = backbone_cfg.get("name", "dinov2_vits14")
    image_size = int(dataset_cfg.get("image_size", backbone_cfg.get("image_size", 518)))
    cache_dir = backbone_cfg.get("cache_dir", "outputs/feature_cache")
    batch = load_feature_cache_if_present(records, cache_dir, cache_name, seed, backbone_name, image_size, cache_seed=cache_seed)
    if batch is not None:
        return batch.patch_features
    backbone = build_backbone(
        backbone_name,
        device=experiment_cfg.get("device", "cuda"),
        image_size=image_size,
        batch_size=int(backbone_cfg.get("batch_size", 8)),
    )
    return encode_with_cache(backbone, records, cache_dir, cache_name, seed, backbone_name, image_size, cache_seed=cache_seed).patch_features


def fit_unweighted(model, support_features: np.ndarray, eval_features: np.ndarray, seed: int, synthetic_ratio: float) -> tuple[np.ndarray, np.ndarray]:
    support_x = model.calibration_features(support_features)
    synth_x = model.synthetic_calibration_features(support_features, seed=seed, ratio=synthetic_ratio)
    train_x = np.concatenate([support_x, synth_x], axis=0)
    train_y = np.concatenate([np.zeros(len(support_x), dtype=np.float32), np.ones(len(synth_x), dtype=np.float32)])
    calibrator = VectorPlattScaler().fit(train_x, train_y, positive_indices=(0,))
    return calibrator.predict_proba(model.calibration_features(eval_features)), train_y


def fit_weighted(model, support_features: np.ndarray, eval_features: np.ndarray, seed: int, synthetic_ratio: float) -> tuple[np.ndarray, float, float]:
    support_x = model.calibration_features(support_features)
    synth_features = model._make_synthetic_feature_batch(support_features, seed=seed, ratio=synthetic_ratio)
    synth_x = model.calibration_features(synth_features)
    _, support_image_cov = pca_patch_covariates(model.pca, support_features)
    test_cov, test_image_cov = pca_patch_covariates(model.pca, eval_features)
    clf = DensityRatioLogistic.fit(support_image_cov, test_image_cov, steps=600)
    normal_w = np.clip(clf.density_ratio(support_image_cov), 0.05, 20.0)
    synth_w = np.full(len(synth_x), float(np.mean(normal_w)), dtype=np.float32)
    train_x = np.concatenate([support_x, synth_x], axis=0)
    train_y = np.concatenate([np.zeros(len(support_x), dtype=np.float32), np.ones(len(synth_x), dtype=np.float32)])
    train_w = np.concatenate([normal_w, synth_w], axis=0)
    calibrator = VectorPlattScaler().fit(train_x, train_y, positive_indices=(0,), sample_weight=train_w)
    probs = calibrator.predict_proba(model.calibration_features(eval_features))
    return probs, effective_sample_size(normal_w), float(clf.probabilities(test_cov).mean())


def eval_case(base_config: dict, dataset: str, cls: str, k: int, seed: int, corruption: str, max_images: int | None, tmp_root: str) -> list[dict]:
    cfg = dict(base_config)
    cfg["dataset"] = {**base_config.get("dataset", {}), "name": dataset, "root": f"data/{dataset}", "classes": [cls], "k_shots": [k], "seeds": [seed]}
    model_cfg = {**base_config.get("model", {}), "pca_components": int(base_config.get("model", {}).get("pca_components", 64))}
    model_cfg.setdefault("device", cfg.get("experiment", {}).get("device", "cuda"))
    records = load_records(dataset, f"data/{dataset}", [cls])
    support = few_shot_support(records, k=k, seed=seed)
    eval_clean = evaluation_records(records)
    tmp_dir = Path(tmp_root) / dataset / cls / f"seed{seed}" / corruption
    eval_corrupt = corrupt_records(eval_clean, corruption, tmp_dir, seed=seed, max_images=max_images)
    backbone_name = cfg.get("backbone", {}).get("name", "dinov2_vits14")
    support_features = get_features(cfg, support, f"{dataset}_support_{backbone_name}_k{k}_seed{seed}", seed)
    corrupt_features = get_features(
        cfg,
        eval_corrupt,
        f"{dataset}_corrupt_{cls}_{corruption}_{backbone_name}_seed{seed}",
        seed,
        cache_seed=0 if backbone_name.startswith("dinov2") else seed,
    )
    base_model = build_model("calib_subspace_head", support_features, model_cfg, seed=seed)
    shift_model = build_model("shift_aware_calib_subspace_head", support_features, model_cfg, seed=seed)
    raw_scores, _ = base_model.score_images(corrupt_features)
    labels = np.asarray([r.label for r in eval_corrupt], dtype=np.int64)
    synthetic_ratio = float(model_cfg.get("synthetic_anomaly_ratio", 1.0))
    vector_probs, _ = fit_unweighted(base_model, support_features, corrupt_features, seed, synthetic_ratio)
    shift_probs, _ = fit_unweighted(shift_model, support_features, corrupt_features, seed, synthetic_ratio)
    weighted_probs, n_eff, domain_conf = fit_weighted(shift_model, support_features, corrupt_features, seed, synthetic_ratio)
    _, test_image_cov = pca_patch_covariates(base_model.pca, corrupt_features)
    pca_patch = base_model.pca.residual_scores(corrupt_features)
    summary = ShiftGateSummary(
        domain_confidence=domain_conf,
        n_eff_ratio=float(n_eff / max(len(support_features), 1)),
        pca_concentration=float(np.mean(pca_patch.max(axis=1) / (pca_patch.mean(axis=1) + 1e-6))),
        residual_std=float(np.std(test_image_cov)),
    )
    expert_probs = np.stack([vector_probs, shift_probs, weighted_probs], axis=1)
    hard_weights = structured_shift_gate(corruption, EXPERTS)
    soft_weights = noise_safe_soft_gate(summary, EXPERTS)
    gate_strength = no_harm_gate_strength(summary, conservative=True)
    adaptive_gate_strength = no_harm_gate_strength(summary, conservative=False)
    candidates = {
        "vector_platt": vector_probs,
        "shift_aware_vector_platt": shift_probs,
        "weighted_platt": weighted_probs,
        "structured_rule_gate": gated_probabilities(expert_probs, hard_weights),
        "soft_neff_gate": gated_probabilities(expert_probs, soft_weights),
        "anchored_structured_gate": anchored_gated_probabilities(vector_probs, expert_probs, hard_weights, gate_strength),
        "anchored_soft_gate": anchored_gated_probabilities(vector_probs, expert_probs, soft_weights, gate_strength),
        "anchored_structured_gate_adaptive": anchored_gated_probabilities(vector_probs, expert_probs, hard_weights, adaptive_gate_strength),
        "anchored_soft_gate_adaptive": anchored_gated_probabilities(vector_probs, expert_probs, soft_weights, adaptive_gate_strength),
    }
    best_method = min(("vector_platt", "shift_aware_vector_platt", "weighted_platt"), key=lambda name: ece_binary(labels, candidates[name]))
    candidates["oracle_best"] = candidates[best_method]
    rows = []
    for method, probs in candidates.items():
        metrics = summarize_binary(labels, raw_scores, probs)
        rows.append(
            {
                "dataset": dataset,
                "class": cls,
                "k_shot": k,
                "seed": seed,
                "corruption": corruption,
                "method": method,
                "oracle_source": best_method if method == "oracle_best" else "",
                "num_images": len(eval_corrupt),
                "n_eff": float(n_eff),
                "n_eff_ratio": summary.n_eff_ratio,
                "domain_confidence": summary.domain_confidence,
                "pca_concentration": summary.pca_concentration,
                "gate_strength": float(gate_strength if method in {"anchored_structured_gate", "anchored_soft_gate"} else adaptive_gate_strength if method in {"anchored_structured_gate_adaptive", "anchored_soft_gate_adaptive"} else np.nan),
                "gate_vector_weight": float(hard_weights[0] if method in {"structured_rule_gate", "anchored_structured_gate", "anchored_structured_gate_adaptive"} else soft_weights[0] if method in {"soft_neff_gate", "anchored_soft_gate", "anchored_soft_gate_adaptive"} else np.nan),
                "gate_shift_weight": float(hard_weights[1] if method in {"structured_rule_gate", "anchored_structured_gate", "anchored_structured_gate_adaptive"} else soft_weights[1] if method in {"soft_neff_gate", "anchored_soft_gate", "anchored_soft_gate_adaptive"} else np.nan),
                "gate_weighted_weight": float(hard_weights[2] if method in {"structured_rule_gate", "anchored_structured_gate", "anchored_structured_gate_adaptive"} else soft_weights[2] if method in {"soft_neff_gate", "anchored_soft_gate", "anchored_soft_gate_adaptive"} else np.nan),
                "entropy_mean": float(entropy_binary(probs).mean()),
                **metrics,
            }
        )
    return rows


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--base-config", default="configs/generated/visa_full/calib_subspace_head_visa_candle_k1_seed0.yaml")
    parser.add_argument("--dataset", default="visa", choices=["visa", "mvtec"])
    parser.add_argument("--classes", nargs="*", default=None)
    parser.add_argument("--k-shots", nargs="*", type=int, default=[4, 8])
    parser.add_argument("--seeds", nargs="*", type=int, default=[0, 1, 2])
    parser.add_argument("--corruptions", nargs="*", default=["gaussian_noise", "blur", "brightness_contrast", "jpeg"])
    parser.add_argument("--max-images", type=int, default=None)
    parser.add_argument("--tmp-root", default="/home/crl/AD/outputs/tmp/gated_shift_corruptions")
    parser.add_argument("--out-dir", default="outputs/paper_tables")
    parser.add_argument("--run-tag", default="representative")
    parser.add_argument("--resume", action="store_true")
    args = parser.parse_args()
    classes = args.classes or (VISA_CLASSES if args.dataset == "visa" else MVTEC_CLASSES)
    base_config = load_config(args.base_config)
    out_dir = Path(args.out_dir)
    detail = out_dir / f"gated_shift_aware_{args.run_tag}_detailed.csv"
    rows = read_existing(detail) if args.resume else []
    done = {(r["dataset"], r["class"], int(r["k_shot"]), int(r["seed"]), r["corruption"]) for r in rows}
    total = len(classes) * len(args.k_shots) * len(args.seeds) * len(args.corruptions)
    for cls in classes:
        for k in args.k_shots:
            for seed in args.seeds:
                for corruption in args.corruptions:
                    key = (args.dataset, cls, k, seed, corruption)
                    if key in done:
                        continue
                    case_rows = eval_case(base_config, args.dataset, cls, k, seed, corruption, args.max_images, args.tmp_root)
                    rows.extend(case_rows)
                    done.add(key)
                    write_csv(detail, rows)
                    summary = summarize(rows, ["dataset", "method", "corruption", "k_shot"], ["auroc", "ap", "ece", "brier", "nll", "entropy_mean", "n_eff", "n_eff_ratio"])
                    delta = delta_rows(summary)
                    oracle_gap = oracle_gap_rows(summary)
                    write_csv(out_dir / f"gated_shift_aware_{args.run_tag}_summary.csv", summary)
                    write_csv(out_dir / f"gated_shift_aware_{args.run_tag}_delta.csv", delta)
                    write_csv(out_dir / f"gated_shift_aware_{args.run_tag}_oracle_gap.csv", oracle_gap)
                    write_csv(out_dir / "gated_shift_aware_summary.csv", summary)
                    write_csv(out_dir / "gated_shift_aware_delta.csv", delta)
                    write_csv(out_dir / "gated_shift_aware_oracle_gap.csv", oracle_gap)
                    print(f"gated_progress={len(done)}/{total} dataset={args.dataset} class={cls} k={k} seed={seed} corruption={corruption}", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
