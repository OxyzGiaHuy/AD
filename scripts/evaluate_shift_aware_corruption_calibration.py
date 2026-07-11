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
from src.calibration.platt import entropy_binary
from src.config import load_config
from src.data.datasets import load_records
from src.data.sampling import evaluation_records, few_shot_support
from src.evaluation.metrics import summarize_binary
from src.models.baselines import build_model
from src.run_experiment import encode_with_cache

METHOD_VARIANTS = {
    "vector_platt": "calib_subspace_head",
    "shift_aware_vector_platt": "shift_aware_calib_subspace_head",
}


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
        key = []
        for group_key in group_keys:
            value = row[group_key]
            if group_key in {"k_shot", "seed"}:
                value = int(value)
            key.append(value)
        groups[tuple(key)].append(row)
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
        key = (row["dataset"], row["corruption"], int(row["k_shot"]))
        by_key[key][row["method"]] = row
    out = []
    for (dataset, corruption, k), methods in sorted(by_key.items(), key=lambda item: tuple(str(v) for v in item[0])):
        if "vector_platt" not in methods or "shift_aware_vector_platt" not in methods:
            continue
        vec = methods["vector_platt"]
        shift = methods["shift_aware_vector_platt"]
        item = {"dataset": dataset, "corruption": corruption, "k_shot": k, "n": shift["n"]}
        for metric in ["auroc", "ap", "ece", "brier", "nll", "entropy_mean"]:
            v = float(vec[f"{metric}_mean"])
            s = float(shift[f"{metric}_mean"])
            item[f"vector_{metric}"] = v
            item[f"shift_aware_{metric}"] = s
            item[f"delta_{metric}_shift_minus_vector"] = s - v
        out.append(item)
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


def eval_case(base_config: dict, dataset: str, cls: str, k: int, seed: int, corruption: str, method: str, max_images: int | None, tmp_root: str) -> dict:
    cfg = dict(base_config)
    cfg["dataset"] = {**base_config.get("dataset", {}), "name": dataset, "root": f"data/{dataset}", "classes": [cls], "k_shots": [k], "seeds": [seed]}
    cfg["model"] = {**base_config.get("model", {}), "variant": METHOD_VARIANTS[method], "pca_components": int(base_config.get("model", {}).get("pca_components", 64))}
    model_cfg = dict(cfg["model"])
    model_cfg.setdefault("device", cfg.get("experiment", {}).get("device", "cuda"))
    records = load_records(dataset, f"data/{dataset}", [cls])
    support = few_shot_support(records, k=k, seed=seed)
    eval_clean = evaluation_records(records)
    tmp_dir = Path(tmp_root) / dataset / cls / f"seed{seed}" / corruption
    eval_corrupt = corrupt_records(eval_clean, corruption, tmp_dir, seed=seed, max_images=max_images)
    backbone_name = cfg.get("backbone", {}).get("name", "dinov2_vits14")
    class_key = cls
    support_features = get_features(cfg, support, f"{dataset}_support_{backbone_name}_k{k}_seed{seed}", seed)
    corrupt_features = get_features(cfg, eval_corrupt, f"{dataset}_corrupt_{class_key}_{corruption}_{backbone_name}_seed{seed}", seed, cache_seed=0 if backbone_name.startswith("dinov2") else seed)
    model = build_model(METHOD_VARIANTS[method], support_features, model_cfg, seed=seed)
    raw_scores, _ = model.score_images(corrupt_features)
    labels = np.asarray([r.label for r in eval_corrupt], dtype=np.int64)
    support_x = model.calibration_features(support_features)
    synth_x = model.synthetic_calibration_features(support_features, seed=seed, ratio=float(model_cfg.get("synthetic_anomaly_ratio", 1.0)))
    eval_x = model.calibration_features(corrupt_features)
    train_x = np.concatenate([support_x, synth_x], axis=0)
    train_y = np.concatenate([np.zeros(len(support_x), dtype=np.float32), np.ones(len(synth_x), dtype=np.float32)])
    from src.calibration.platt import VectorPlattScaler

    calibrator = VectorPlattScaler().fit(train_x, train_y, positive_indices=(0,))
    probs = calibrator.predict_proba(eval_x)
    metrics = summarize_binary(labels, raw_scores, probs, bins=int(cfg.get("calibration", {}).get("bins", 15)))
    return {
        "dataset": dataset,
        "class": cls,
        "k_shot": k,
        "seed": seed,
        "corruption": corruption,
        "method": method,
        "variant": METHOD_VARIANTS[method],
        "num_images": len(eval_corrupt),
        "entropy_mean": float(entropy_binary(probs).mean()),
        "feature_dim": int(eval_x.shape[1]),
        **metrics,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--base-config", default="configs/generated/visa_full/calib_subspace_head_visa_candle_k1_seed0.yaml")
    parser.add_argument("--dataset", default="visa", choices=["visa", "mvtec"])
    parser.add_argument("--classes", nargs="*", default=None)
    parser.add_argument("--k-shots", nargs="*", type=int, default=[1, 2, 4, 8])
    parser.add_argument("--seeds", nargs="*", type=int, default=[0, 1, 2, 3, 4])
    parser.add_argument("--corruptions", nargs="*", default=["gaussian_noise", "blur", "brightness_contrast", "jpeg"])
    parser.add_argument("--methods", nargs="*", default=["vector_platt", "shift_aware_vector_platt"], choices=sorted(METHOD_VARIANTS))
    parser.add_argument("--max-images", type=int, default=None)
    parser.add_argument("--tmp-root", default="/tmp/AD-shift-aware-corruptions")
    parser.add_argument("--out-dir", default="outputs/paper_tables")
    parser.add_argument("--run-tag", default="representative")
    parser.add_argument("--resume", action="store_true")
    args = parser.parse_args()
    classes = args.classes or (VISA_CLASSES if args.dataset == "visa" else MVTEC_CLASSES)
    base_config = load_config(args.base_config)
    out_dir = Path(args.out_dir)
    detail = out_dir / f"shift_aware_corruption_calibration_{args.run_tag}_detailed.csv"
    rows = read_existing(detail) if args.resume else []
    done = {(r["dataset"], r["class"], int(r["k_shot"]), int(r["seed"]), r["corruption"], r["method"]) for r in rows}
    total = len(classes) * len(args.k_shots) * len(args.seeds) * len(args.corruptions) * len(args.methods)
    for cls in classes:
        for k in args.k_shots:
            for seed in args.seeds:
                for corruption in args.corruptions:
                    for method in args.methods:
                        key = (args.dataset, cls, k, seed, corruption, method)
                        if key in done:
                            continue
                        row = eval_case(base_config, args.dataset, cls, k, seed, corruption, method, args.max_images, args.tmp_root)
                        rows.append(row)
                        done.add(key)
                        write_csv(detail, rows)
                        summary = summarize(rows, ["dataset", "method", "corruption", "k_shot"], ["auroc", "ap", "ece", "brier", "nll", "entropy_mean"])
                        write_csv(out_dir / f"shift_aware_corruption_calibration_{args.run_tag}_summary.csv", summary)
                        write_csv(out_dir / f"shift_aware_corruption_calibration_{args.run_tag}_delta.csv", delta_rows(summary))
                        print(f"shift_corruption_progress={len(rows)}/{total} dataset={args.dataset} class={cls} k={k} seed={seed} corruption={corruption} method={method}", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
