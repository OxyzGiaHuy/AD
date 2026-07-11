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
from src.config import load_config
from src.conformal import (
    DensityRatioLogistic,
    benjamini_hochberg_mask,
    conformal_p_values,
    effective_sample_size,
    insample_calibration,
    loio_calibration,
    pca_patch_covariates,
    top_fraction_score,
    weighted_conformal_p_values,
)
from src.data.datasets import load_records
from src.data.sampling import evaluation_records, few_shot_support
from src.evaluation.metrics import average_precision_np, roc_auc_score_np
from src.models.pca import PCASubspace
from src.run_experiment import encode_with_cache


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


def weighted_delta(summary_rows: list[dict]) -> list[dict]:
    by_key: dict[tuple, dict[str, dict]] = defaultdict(dict)
    for row in summary_rows:
        key = (row["dataset"], row["corruption"], row["k_shot"])
        by_key[key][row["mode"]] = row
    out = []
    for (dataset, corruption, k), modes in sorted(by_key.items(), key=lambda item: tuple(str(v) for v in item[0])):
        if "loio_conformal" not in modes or "weighted_conformal" not in modes:
            continue
        base = modes["loio_conformal"]
        weighted = modes["weighted_conformal"]
        item = {"dataset": dataset, "corruption": corruption, "k_shot": k, "n": weighted["n"]}
        for metric in ["false_alarm_rate", "coverage_gap", "image_p_auroc", "image_p_ap", "patch_rejection_rate", "n_eff_patch"]:
            b = float(base[f"{metric}_mean"])
            w = float(weighted[f"{metric}_mean"])
            item[f"loio_{metric}"] = b
            item[f"weighted_{metric}"] = w
            item[f"delta_{metric}_weighted_minus_loio"] = w - b
        out.append(item)
    return out




def sample_rows(x: np.ndarray, max_rows: int, seed: int) -> np.ndarray:
    if len(x) <= max_rows:
        return x
    rng = np.random.default_rng(seed)
    idx = rng.choice(len(x), size=max_rows, replace=False)
    return x[idx]

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


def eval_case(
    base_config: dict,
    dataset: str,
    cls: str,
    k: int,
    seed: int,
    corruption: str,
    mode: str,
    max_images: int | None,
    tmp_root: str,
    alpha: float,
    q: float,
    rho: float,
) -> dict:
    cfg = dict(base_config)
    cfg["dataset"] = {**base_config.get("dataset", {}), "name": dataset, "root": f"data/{dataset}", "classes": [cls], "k_shots": [k], "seeds": [seed]}
    pca_components = int(base_config.get("model", {}).get("pca_components", 64))
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
    pca = PCASubspace.fit(support_features, pca_components)
    patch_scores = pca.residual_scores(corrupt_features).astype(np.float32)
    image_scores = top_fraction_score(patch_scores, rho=rho)
    labels = np.asarray([r.label for r in eval_corrupt], dtype=np.int64)
    if mode == "insample_conformal":
        cal = insample_calibration(support_features, pca_components, rho=rho)
        patch_p = conformal_p_values(cal.patch_scores, patch_scores.reshape(-1)).reshape(patch_scores.shape)
        image_p = conformal_p_values(cal.image_scores, image_scores)
        n_eff_patch = float(len(cal.patch_scores))
        n_eff_image = float(len(cal.image_scores))
        domain_conf = float("nan")
    elif mode == "loio_conformal":
        cal = loio_calibration(support_features, pca_components, rho=rho)
        patch_p = conformal_p_values(cal.patch_scores, patch_scores.reshape(-1)).reshape(patch_scores.shape)
        image_p = conformal_p_values(cal.image_scores, image_scores)
        n_eff_patch = float(len(cal.patch_scores))
        n_eff_image = float(len(cal.image_scores))
        domain_conf = float("nan")
    elif mode == "weighted_conformal":
        cal = loio_calibration(support_features, pca_components, rho=rho)
        test_cov, test_image_cov = pca_patch_covariates(pca, corrupt_features)
        clf = DensityRatioLogistic.fit(sample_rows(cal.patch_covariates, 20_000, seed), sample_rows(test_cov, 20_000, seed + 17), steps=600)
        patch_w = np.clip(clf.density_ratio(cal.patch_covariates), 0.05, 20.0)
        test_patch_w = np.clip(clf.density_ratio(test_cov), 0.05, 20.0)
        image_clf = DensityRatioLogistic.fit(cal.image_covariates, sample_rows(test_image_cov, 20_000, seed + 31), steps=600)
        image_w = np.clip(image_clf.density_ratio(cal.image_covariates), 0.05, 20.0)
        test_image_w = np.clip(image_clf.density_ratio(test_image_cov), 0.05, 20.0)
        patch_p = weighted_conformal_p_values(cal.patch_scores, patch_scores.reshape(-1), patch_w, test_patch_w).reshape(patch_scores.shape)
        image_p = weighted_conformal_p_values(cal.image_scores, image_scores, image_w, test_image_w)
        n_eff_patch = effective_sample_size(patch_w)
        n_eff_image = effective_sample_size(image_w)
        domain_conf = float(clf.probabilities(test_cov).mean())
    else:
        raise ValueError(f"Unknown mode: {mode}")
    pred = image_p <= alpha
    normal_mask = labels == 0
    anomaly_mask = labels == 1
    bh_mask = benjamini_hochberg_mask(patch_p, q=q)
    false_alarm = float(np.mean(pred[normal_mask])) if np.any(normal_mask) else float("nan")
    anomaly_detection = float(np.mean(pred[anomaly_mask])) if np.any(anomaly_mask) else float("nan")
    return {
        "dataset": dataset,
        "class": cls,
        "k_shot": k,
        "seed": seed,
        "corruption": corruption,
        "mode": mode,
        "num_images": len(eval_corrupt),
        "num_calibration_patches": int(len(cal.patch_scores)),
        "num_calibration_images": int(len(cal.image_scores)),
        "alpha": alpha,
        "q": q,
        "rho": rho,
        "false_alarm_rate": false_alarm,
        "anomaly_detection_rate": anomaly_detection,
        "coverage_gap": false_alarm - alpha if np.isfinite(false_alarm) else float("nan"),
        "image_p_auroc": roc_auc_score_np(labels, -image_p),
        "image_p_ap": average_precision_np(labels, -image_p),
        "raw_auroc": roc_auc_score_np(labels, image_scores),
        "raw_ap": average_precision_np(labels, image_scores),
        "patch_rejection_rate": float(np.mean(bh_mask)),
        "image_p_mean_normal": float(image_p[normal_mask].mean()) if np.any(normal_mask) else float("nan"),
        "image_p_mean_anomaly": float(image_p[anomaly_mask].mean()) if np.any(anomaly_mask) else float("nan"),
        "n_eff_patch": float(n_eff_patch),
        "n_eff_image": float(n_eff_image),
        "domain_confidence": domain_conf,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--base-config", default="configs/generated/visa_full/calib_subspace_head_visa_candle_k1_seed0.yaml")
    parser.add_argument("--dataset", default="visa", choices=["visa", "mvtec"])
    parser.add_argument("--classes", nargs="*", default=None)
    parser.add_argument("--k-shots", nargs="*", type=int, default=[4, 8])
    parser.add_argument("--seeds", nargs="*", type=int, default=[0, 1, 2])
    parser.add_argument("--corruptions", nargs="*", default=["gaussian_noise", "blur", "brightness_contrast", "jpeg"])
    parser.add_argument("--modes", nargs="*", default=["insample_conformal", "loio_conformal", "weighted_conformal"])
    parser.add_argument("--max-images", type=int, default=None)
    parser.add_argument("--tmp-root", default="/home/crl/AD/outputs/tmp/sw_cad_corruptions")
    parser.add_argument("--out-dir", default="outputs/paper_tables")
    parser.add_argument("--run-tag", default="representative")
    parser.add_argument("--alpha", type=float, default=0.1)
    parser.add_argument("--q", type=float, default=0.1)
    parser.add_argument("--rho", type=float, default=0.01)
    parser.add_argument("--resume", action="store_true")
    args = parser.parse_args()
    classes = args.classes or (VISA_CLASSES if args.dataset == "visa" else MVTEC_CLASSES)
    base_config = load_config(args.base_config)
    out_dir = Path(args.out_dir)
    detail = out_dir / f"sw_cad_conformal_{args.run_tag}_detailed.csv"
    rows = read_existing(detail) if args.resume else []
    done = {(r["dataset"], r["class"], int(r["k_shot"]), int(r["seed"]), r["corruption"], r["mode"]) for r in rows}
    total = len(classes) * len(args.k_shots) * len(args.seeds) * len(args.corruptions) * len(args.modes)
    for cls in classes:
        for k in args.k_shots:
            for seed in args.seeds:
                for corruption in args.corruptions:
                    for mode in args.modes:
                        key = (args.dataset, cls, k, seed, corruption, mode)
                        if key in done:
                            continue
                        row = eval_case(base_config, args.dataset, cls, k, seed, corruption, mode, args.max_images, args.tmp_root, args.alpha, args.q, args.rho)
                        rows.append(row)
                        done.add(key)
                        write_csv(detail, rows)
                        summary = summarize(
                            rows,
                            ["dataset", "mode", "corruption", "k_shot"],
                            ["false_alarm_rate", "coverage_gap", "image_p_auroc", "image_p_ap", "raw_auroc", "raw_ap", "patch_rejection_rate", "n_eff_patch", "n_eff_image"],
                        )
                        write_csv(out_dir / "sw_cad_conformal_summary.csv", summary)
                        write_csv(out_dir / "sw_cad_weighted_conformal_delta.csv", weighted_delta(summary))
                        print(f"sw_cad_progress={len(rows)}/{total} dataset={args.dataset} class={cls} k={k} seed={seed} corruption={corruption} mode={mode}", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
