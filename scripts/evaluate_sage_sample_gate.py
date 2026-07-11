from __future__ import annotations

import argparse
import csv
from collections import Counter, defaultdict
from pathlib import Path
import sys

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.evaluate_corruptions import corrupt_records, load_feature_cache_if_present
from scripts.generate_benchmark_grid import MVTEC_CLASSES, VISA_CLASSES
from src.backbones.dinov2 import build_backbone
from src.calibration.offline_sage_gate import BrierMixtureGate, RidgeECERegressor, SoftmaxLinearGate, risk_aware_choice, standardize_train_test
from src.calibration.platt import VectorPlattScaler, entropy_binary
from src.config import load_config
from src.conformal import DensityRatioLogistic, effective_sample_size, pca_patch_covariates
from src.data.datasets import load_records
from src.data.sampling import evaluation_records, few_shot_support
from src.evaluation.metrics import ece_binary, summarize_binary
from src.models.baselines import build_model
from src.run_experiment import encode_with_cache

EXPERTS = ["vector_platt", "shift_aware_vector_platt", "weighted_platt", "anchored_structured_gate"]
REPRESENTATIVE = {
    "visa": ["candle", "cashew", "pcb1", "pipe_fryum"],
    "mvtec": ["bottle", "cable", "hazelnut"],
}


def write_csv(path: Path, rows: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not rows:
        path.write_text("", encoding="utf-8")
        return
    fieldnames = list(rows[0].keys())
    for row in rows[1:]:
        for key in row.keys():
            if key not in fieldnames:
                fieldnames.append(key)
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def read_existing(path: Path) -> list[dict]:
    if not path.exists() or path.stat().st_size == 0:
        return []
    with path.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


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


def fit_unweighted(model, support_features: np.ndarray, eval_features: np.ndarray, seed: int, synthetic_ratio: float) -> np.ndarray:
    support_x = model.calibration_features(support_features)
    synth_x = model.synthetic_calibration_features(support_features, seed=seed, ratio=synthetic_ratio)
    train_x = np.concatenate([support_x, synth_x], axis=0)
    train_y = np.concatenate([np.zeros(len(support_x), dtype=np.float32), np.ones(len(synth_x), dtype=np.float32)])
    calibrator = VectorPlattScaler().fit(train_x, train_y, positive_indices=(0,))
    return calibrator.predict_proba(model.calibration_features(eval_features))


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


def anchored_structured(vector_probs: np.ndarray, shift_probs: np.ndarray, weighted_probs: np.ndarray, corruption: str, strength: float) -> np.ndarray:
    if corruption == "gaussian_noise":
        target = vector_probs
    elif corruption in {"blur", "brightness_contrast", "jpeg"}:
        target = shift_probs
    else:
        target = 0.5 * shift_probs + 0.5 * weighted_probs
    return np.clip(vector_probs + strength * (target - vector_probs), 0.0, 1.0)


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
    vector_probs = fit_unweighted(base_model, support_features, corrupt_features, seed, synthetic_ratio)
    shift_probs = fit_unweighted(shift_model, support_features, corrupt_features, seed, synthetic_ratio)
    weighted_probs, n_eff, domain_conf = fit_weighted(shift_model, support_features, corrupt_features, seed, synthetic_ratio)
    pca_patch = base_model.pca.residual_scores(corrupt_features)
    n_eff_ratio = float(n_eff / max(len(support_features), 1))
    pca_concentration = float(np.mean(pca_patch.max(axis=1) / (pca_patch.mean(axis=1) + 1e-6)))
    domain_shift_strength = float(2.0 * abs(domain_conf - 0.5))
    noisy_signal = float(np.clip((pca_concentration - 4.0) / 4.0, 0.0, 1.0))
    strength = float(np.clip(n_eff_ratio * domain_shift_strength * (1.0 - 0.75 * noisy_signal), 0.0, 1.0))
    anchored_probs = anchored_structured(vector_probs, shift_probs, weighted_probs, corruption, strength)
    rows = []
    for i, rec in enumerate(eval_corrupt):
        probs = {
            "vector_platt": float(vector_probs[i]),
            "shift_aware_vector_platt": float(shift_probs[i]),
            "weighted_platt": float(weighted_probs[i]),
            "anchored_structured_gate": float(anchored_probs[i]),
        }
        entropy_vals = {f"entropy_{name}": float(entropy_binary(np.asarray([prob], dtype=np.float32))[0]) for name, prob in probs.items()}
        rows.append(
            {
                "dataset": dataset,
                "class": cls,
                "k_shot": k,
                "seed": seed,
                "corruption": corruption,
                "image_path": str(rec.path),
                "label": int(labels[i]),
                "raw_score": float(raw_scores[i]),
                "n_eff": float(n_eff),
                "n_eff_ratio": n_eff_ratio,
                "domain_confidence": float(domain_conf),
                "domain_shift_strength": domain_shift_strength,
                "pca_concentration": pca_concentration,
                "gate_strength": strength,
                "expert_disagreement": float(np.max(list(probs.values())) - np.min(list(probs.values()))),
                **probs,
                **entropy_vals,
            }
        )
    return rows


def one_hot(value: str, choices: list[str]) -> list[float]:
    return [1.0 if value == c else 0.0 for c in choices]


def build_arrays(rows: list[dict], experts: list[str]) -> tuple[np.ndarray, np.ndarray, np.ndarray, list[tuple], list[str]]:
    corruptions = sorted({r["corruption"] for r in rows})
    datasets = sorted({r["dataset"] for r in rows})
    feature_names = [
        "log_k",
        "seed_scaled",
        "raw_score",
        "n_eff_ratio",
        "domain_shift_strength",
        "domain_confidence",
        "pca_concentration",
        "gate_strength",
        "expert_disagreement",
    ] + [f"p_{e}" for e in experts] + [f"entropy_{e}" for e in experts] + [f"corr={c}" for c in corruptions] + [f"dataset={d}" for d in datasets]
    x = []
    y = []
    probs = []
    keys = []
    for r in rows:
        p = [float(r[e]) for e in experts]
        ent = [float(r[f"entropy_{e}"]) for e in experts]
        x.append(
            [
                np.log(float(r["k_shot"])),
                float(r["seed"]) / 4.0,
                float(r["raw_score"]),
                float(r["n_eff_ratio"]),
                float(r["domain_shift_strength"]),
                float(r["domain_confidence"]),
                float(r["pca_concentration"]),
                float(r["gate_strength"]),
                float(r["expert_disagreement"]),
            ]
            + p
            + ent
            + one_hot(r["corruption"], corruptions)
            + one_hot(r["dataset"], datasets)
        )
        y.append(int(r["label"]))
        probs.append(p)
        keys.append((r["dataset"], r["class"], int(r["k_shot"]), int(r["seed"]), r["corruption"], r["image_path"]))
    return np.asarray(x, dtype=np.float64), np.asarray(y, dtype=np.int64), np.asarray(probs, dtype=np.float64), keys, feature_names


def binary_nll(y: np.ndarray, p: np.ndarray) -> np.ndarray:
    p = np.clip(p, 1e-6, 1.0 - 1e-6)
    return -(y * np.log(p) + (1 - y) * np.log(1 - p))


def choose_oracle(y: np.ndarray, probs: np.ndarray, objective: str) -> np.ndarray:
    if objective == "brier":
        losses = (probs - y[:, None]) ** 2
    else:
        losses = np.stack([binary_nll(y, probs[:, i]) for i in range(probs.shape[1])], axis=1)
    return losses.argmin(axis=1)


def summarize_predictions(name: str, split: str, y: np.ndarray, raw: np.ndarray, pred_prob: np.ndarray, chosen: np.ndarray | None, experts: list[str]) -> dict:
    metrics = summarize_binary(y, raw, pred_prob)
    usage = Counter(experts[int(i)] for i in chosen) if chosen is not None else Counter()
    vector_ece = ece_binary(y, raw * 0 + pred_prob) if False else np.nan
    return {
        "gate": name,
        "split": split,
        "n_images": len(y),
        "auroc": metrics["auroc"],
        "ap": metrics["ap"],
        "ece": metrics["ece"],
        "brier": metrics["brier"],
        "nll": metrics["nll"],
        "usage": ";".join(f"{e}:{usage.get(e, 0)}" for e in experts) if chosen is not None else "",
    }


def evaluate_split(rows: list[dict], train_idx: np.ndarray, test_idx: np.ndarray, split: str, experts: list[str]) -> list[dict]:
    x, y, probs, keys, _ = build_arrays(rows, experts)
    raw = np.asarray([float(r["raw_score"]) for r in rows], dtype=np.float64)
    x_train, x_test, _, _ = standardize_train_test(x[train_idx], x[test_idx])
    y_train, y_test = y[train_idx], y[test_idx]
    probs_train, probs_test = probs[train_idx], probs[test_idx]
    raw_test = raw[test_idx]
    anchor_idx = experts.index("vector_platt")
    out = []
    for i, e in enumerate(experts):
        out.append(summarize_predictions(e, split, y_test, raw_test, probs_test[:, i], np.full(len(test_idx), i), experts))
    oracle = choose_oracle(y_test, probs_test, objective="nll")
    out.append(summarize_predictions("oracle_sample_best_nll", split, y_test, raw_test, probs_test[np.arange(len(test_idx)), oracle], oracle, experts))

    y_best = choose_oracle(y_train, probs_train, objective="nll")
    gate = SoftmaxLinearGate(lr=0.03, steps=1500, l2=1e-3, seed=17).fit(x_train, y_best)
    choice = gate.predict(x_test)
    out.append(summarize_predictions("sample_logistic_top1_nll", split, y_test, raw_test, probs_test[np.arange(len(test_idx)), choice], choice, experts))

    train_losses = np.stack([binary_nll(y_train, probs_train[:, i]) for i in range(len(experts))], axis=1)
    reg = RidgeECERegressor(l2=0.1).fit(x_train, train_losses)
    pred_loss = reg.predict(x_test)
    for margin in [0.0, 0.005, 0.01, 0.02]:
        choice = risk_aware_choice(pred_loss, anchor_idx, margin=margin)
        out.append(summarize_predictions(f"sample_risk_margin_{margin:g}", split, y_test, raw_test, probs_test[np.arange(len(test_idx)), choice], choice, experts))

    dynamic_labels = (train_losses.min(axis=1) < train_losses[:, anchor_idx] - 0.005).astype(np.int64)
    if dynamic_labels.max() == dynamic_labels.min():
        dyn_prob = np.full(len(test_idx), float(dynamic_labels[0]), dtype=np.float64)
    else:
        shared = SoftmaxLinearGate(lr=0.03, steps=1000, l2=1e-3, seed=19).fit(x_train, dynamic_labels)
        dyn_prob = shared.predict_proba(x_test)[:, 1]
    dyn_indices = [i for i in range(len(experts)) if i != anchor_idx]
    dyn_train_losses = train_losses[:, dyn_indices]
    dyn_y = dyn_train_losses.argmin(axis=1)
    dyn_gate = SoftmaxLinearGate(lr=0.03, steps=1000, l2=1e-3, seed=23).fit(x_train, dyn_y)
    dyn_probs = dyn_gate.predict_proba(x_test)
    for threshold in [0.5, 0.6, 0.7, 0.8]:
        choice = np.full(len(test_idx), anchor_idx, dtype=np.int64)
        use_dyn = dyn_prob >= threshold
        if np.any(use_dyn):
            choice[use_dyn] = np.asarray(dyn_indices, dtype=np.int64)[dyn_probs[use_dyn].argmax(axis=1)]
        out.append(summarize_predictions(f"sample_sage_hier_t{threshold:g}", split, y_test, raw_test, probs_test[np.arange(len(test_idx)), choice], choice, experts))

    mixture_specs = [
        ("sample_brier_mix", dict(no_harm=0.0, anchor_reg=0.0)),
        ("sample_brier_anchor_reg", dict(no_harm=0.0, anchor_reg=0.25)),
        ("sample_brier_noharm", dict(no_harm=2.0, anchor_reg=0.0)),
        ("sample_brier_noharm_anchor", dict(no_harm=2.0, anchor_reg=0.25)),
    ]
    for name, kwargs in mixture_specs:
        mix_gate = BrierMixtureGate(lr=0.05, steps=1800, l2=1e-3, seed=29, **kwargs).fit(x_train, probs_train, y_train, anchor_index=anchor_idx)
        mixed_prob = mix_gate.predict_proba(x_test, probs_test)
        weights = mix_gate.predict_weights(x_test)
        pseudo_choice = weights.argmax(axis=1)
        item = summarize_predictions(name, split, y_test, raw_test, mixed_prob, pseudo_choice, experts)
        item["mean_gate_entropy"] = float((-weights * np.log(np.clip(weights, 1e-12, 1.0))).sum(axis=1).mean())
        item["mean_anchor_weight"] = float(weights[:, anchor_idx].mean())
        out.append(item)
    return out


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--base-config", default="configs/generated/visa_full/calib_subspace_head_visa_candle_k1_seed0.yaml")
    parser.add_argument("--datasets", nargs="*", default=["visa", "mvtec"], choices=["visa", "mvtec"])
    parser.add_argument("--classes", nargs="*", default=None, help="Optional class list shared across selected datasets; defaults to representative classes.")
    parser.add_argument("--k-shots", nargs="*", type=int, default=[4, 8])
    parser.add_argument("--seeds", nargs="*", type=int, default=[0, 1])
    parser.add_argument("--corruptions", nargs="*", default=["gaussian_noise", "blur", "brightness_contrast", "jpeg"])
    parser.add_argument("--max-images", type=int, default=120)
    parser.add_argument("--tmp-root", default="/home/crl/AD/tmp/sage_sample_gate_corruptions")
    parser.add_argument("--out-dir", default="outputs/paper_tables")
    parser.add_argument("--run-tag", default="sage_sample_gate_representative")
    parser.add_argument("--resume", action="store_true")
    args = parser.parse_args()

    base_config = load_config(args.base_config)
    out_dir = Path(args.out_dir)
    pred_path = out_dir / f"{args.run_tag}_predictions.csv"
    rows = read_existing(pred_path) if args.resume else []
    done = {(r["dataset"], r["class"], int(r["k_shot"]), int(r["seed"]), r["corruption"]) for r in rows}
    total = 0
    jobs = []
    for dataset in args.datasets:
        classes = args.classes or REPRESENTATIVE[dataset]
        valid = VISA_CLASSES if dataset == "visa" else MVTEC_CLASSES
        classes = [c for c in classes if c in valid]
        for cls in classes:
            for k in args.k_shots:
                for seed in args.seeds:
                    for corruption in args.corruptions:
                        jobs.append((dataset, cls, k, seed, corruption))
    total = len(jobs)
    for dataset, cls, k, seed, corruption in jobs:
        key = (dataset, cls, k, seed, corruption)
        if key in done:
            continue
        rows.extend(eval_case(base_config, dataset, cls, k, seed, corruption, args.max_images, args.tmp_root))
        done.add(key)
        write_csv(pred_path, rows)
        print(f"sample_gate_progress={len(done)}/{total} dataset={dataset} class={cls} k={k} seed={seed} corruption={corruption}", flush=True)

    experts = EXPERTS
    all_rows = rows
    eval_rows = []
    # Leave-one-class-out within each dataset.
    for dataset in sorted({r["dataset"] for r in all_rows}):
        classes = sorted({r["class"] for r in all_rows if r["dataset"] == dataset})
        for cls in classes:
            train_idx = np.asarray([i for i, r in enumerate(all_rows) if not (r["dataset"] == dataset and r["class"] == cls)], dtype=np.int64)
            test_idx = np.asarray([i for i, r in enumerate(all_rows) if r["dataset"] == dataset and r["class"] == cls], dtype=np.int64)
            eval_rows.extend(evaluate_split(all_rows, train_idx, test_idx, f"loco:{dataset}:{cls}", experts))
    for train_dataset, test_dataset in [("visa", "mvtec"), ("mvtec", "visa")]:
        train_idx = np.asarray([i for i, r in enumerate(all_rows) if r["dataset"] == train_dataset], dtype=np.int64)
        test_idx = np.asarray([i for i, r in enumerate(all_rows) if r["dataset"] == test_dataset], dtype=np.int64)
        if len(train_idx) and len(test_idx):
            eval_rows.extend(evaluate_split(all_rows, train_idx, test_idx, f"cross:{train_dataset}_to_{test_dataset}", experts))
    write_csv(out_dir / f"{args.run_tag}_evaluation.csv", eval_rows)
    print(f"wrote {len(rows)} predictions and {len(eval_rows)} evaluation rows")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
