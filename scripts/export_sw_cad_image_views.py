from __future__ import annotations

import argparse
import csv
from pathlib import Path
import sys

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.evaluate_corruptions import corrupt_records, load_feature_cache_if_present
from scripts.evaluate_sw_cad import sample_rows
from scripts.generate_benchmark_grid import MVTEC_CLASSES, VISA_CLASSES
from src.backbones.dinov2 import build_backbone
from src.config import load_config
from src.conformal import DensityRatioLogistic, benjamini_hochberg_mask, conformal_p_values, effective_sample_size, loio_calibration, pca_patch_covariates, top_fraction_score, weighted_conformal_p_values
from src.data.datasets import load_records
from src.data.sampling import evaluation_records, few_shot_support
from src.models.pca import PCASubspace
from src.run_experiment import encode_with_cache

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
        for key in row:
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
    backbone = build_backbone(backbone_name, device=experiment_cfg.get("device", "cuda"), image_size=image_size, batch_size=int(backbone_cfg.get("batch_size", 8)))
    return encode_with_cache(backbone, records, cache_dir, cache_name, seed, backbone_name, image_size, cache_seed=cache_seed).patch_features


def eval_case(base_config: dict, dataset: str, cls: str, k: int, seed: int, corruption: str, max_images: int | None, tmp_root: str, alpha: float, q: float, rho: float) -> list[dict]:
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
    corrupt_features = get_features(cfg, eval_corrupt, f"{dataset}_corrupt_{cls}_{corruption}_{backbone_name}_seed{seed}", seed, cache_seed=0 if backbone_name.startswith("dinov2") else seed)
    pca = PCASubspace.fit(support_features, pca_components)
    patch_scores = pca.residual_scores(corrupt_features).astype(np.float32)
    image_scores = top_fraction_score(patch_scores, rho=rho)
    cal = loio_calibration(support_features, pca_components, rho=rho)
    patch_p_loio = conformal_p_values(cal.patch_scores, patch_scores.reshape(-1)).reshape(patch_scores.shape)
    image_p_loio = conformal_p_values(cal.image_scores, image_scores)
    test_cov, test_image_cov = pca_patch_covariates(pca, corrupt_features)
    clf = DensityRatioLogistic.fit(sample_rows(cal.patch_covariates, 20_000, seed), sample_rows(test_cov, 20_000, seed + 17), steps=300)
    patch_w = np.clip(clf.density_ratio(cal.patch_covariates), 0.05, 20.0)
    test_patch_w = np.clip(clf.density_ratio(test_cov), 0.05, 20.0)
    image_clf = DensityRatioLogistic.fit(cal.image_covariates, sample_rows(test_image_cov, 20_000, seed + 31), steps=300)
    image_w = np.clip(image_clf.density_ratio(cal.image_covariates), 0.05, 20.0)
    test_image_w = np.clip(image_clf.density_ratio(test_image_cov), 0.05, 20.0)
    # Image-level weighted conformal is cheap and is the main conformal view expert.
    # Full weighted patch p-values are expensive for representative grids, so we
    # keep patch rejection from LOIO and mark weighted patch rejection as NaN.
    image_p_weighted = weighted_conformal_p_values(cal.image_scores, image_scores, image_w, test_image_w)
    patch_reject_loio = benjamini_hochberg_mask(patch_p_loio, q=q).mean(axis=1)
    patch_reject_weighted = np.full(len(eval_corrupt), float("nan"), dtype=np.float32)
    labels = np.asarray([r.label for r in eval_corrupt], dtype=np.int64)
    normal = labels == 0
    coverage_gap_proxy = float(np.mean(image_p_loio[normal] <= alpha) - alpha) if np.any(normal) else float("nan")
    n_eff_patch = effective_sample_size(patch_w)
    n_eff_image = effective_sample_size(image_w)
    rows = []
    for i, rec in enumerate(eval_corrupt):
        rows.append({
            "dataset": dataset,
            "class": cls,
            "k_shot": k,
            "seed": seed,
            "corruption": corruption,
            "image_path": str(rec.path),
            "label": int(labels[i]),
            "raw_score": float(image_scores[i]),
            "image_p_loio": float(image_p_loio[i]),
            "image_p_weighted": float(image_p_weighted[i]),
            "conformal_prob_loio": float(1.0 - image_p_loio[i]),
            "conformal_prob_weighted": float(1.0 - image_p_weighted[i]),
            "patch_rejection_rate_loio": float(patch_reject_loio[i]),
            "patch_rejection_rate_weighted": float(patch_reject_weighted[i]),
            "n_eff_patch": float(n_eff_patch),
            "n_eff_image": float(n_eff_image),
            "coverage_gap_proxy": coverage_gap_proxy,
            "domain_confidence_conformal": float(clf.probabilities(test_cov).mean()),
        })
    return rows


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--base-config", default="configs/generated/visa_full/calib_subspace_head_visa_candle_k1_seed0.yaml")
    parser.add_argument("--dataset", default="visa", choices=["visa", "mvtec"])
    parser.add_argument("--classes", nargs="*", default=None)
    parser.add_argument("--k-shots", nargs="*", type=int, default=[4, 8])
    parser.add_argument("--seeds", nargs="*", type=int, default=[0, 1])
    parser.add_argument("--corruptions", nargs="*", default=["gaussian_noise", "blur", "brightness_contrast", "jpeg"])
    parser.add_argument("--max-images", type=int, default=None)
    parser.add_argument("--tmp-root", default="/home/crl/AD/tmp/sw_cad_image_views")
    parser.add_argument("--out-dir", default="outputs/paper_tables")
    parser.add_argument("--run-tag", default="representative")
    parser.add_argument("--alpha", type=float, default=0.1)
    parser.add_argument("--q", type=float, default=0.1)
    parser.add_argument("--rho", type=float, default=0.01)
    parser.add_argument("--resume", action="store_true")
    args = parser.parse_args()
    base_config = load_config(args.base_config)
    classes = args.classes or REPRESENTATIVE.get(args.dataset) or (VISA_CLASSES if args.dataset == "visa" else MVTEC_CLASSES)
    out_path = Path(args.out_dir) / f"sw_cad_image_views_{args.run_tag}.csv"
    rows = read_existing(out_path) if args.resume else []
    done = {(r["dataset"], r["class"], int(r["k_shot"]), int(r["seed"]), r["corruption"]) for r in rows}
    jobs = [(args.dataset, cls, k, seed, corr) for cls in classes for k in args.k_shots for seed in args.seeds for corr in args.corruptions]
    for dataset, cls, k, seed, corr in jobs:
        key = (dataset, cls, k, seed, corr)
        if key in done:
            continue
        rows.extend(eval_case(base_config, dataset, cls, k, seed, corr, args.max_images, args.tmp_root, args.alpha, args.q, args.rho))
        done.add(key)
        write_csv(out_path, rows)
        print(f"swcad_view_progress={len(done)}/{len(jobs)} dataset={dataset} class={cls} k={k} seed={seed} corruption={corr}", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
