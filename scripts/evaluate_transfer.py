from __future__ import annotations

import argparse
import csv
import fcntl
from pathlib import Path
import sys

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.generate_benchmark_grid import MVTEC_CLASSES, VISA_CLASSES
from src.calibration.platt import VectorPlattScaler, entropy_binary
from src.config import load_config
from src.data.datasets import load_records
from src.data.sampling import evaluation_records, few_shot_support
from src.evaluation.metrics import summarize_binary
from src.models.baselines import build_model
from src.run_experiment import encode_with_cache, load_feature_cache_if_present


def feature_settings(config: dict) -> tuple[str, int, str, str, int]:
    dataset_cfg = config.get("dataset", {})
    backbone_cfg = config.get("backbone", {})
    experiment_cfg = config.get("experiment", {})
    backbone_name = backbone_cfg.get("name", "dinov2_vits14")
    image_size = int(dataset_cfg.get("image_size", backbone_cfg.get("image_size", 518)))
    cache_dir = backbone_cfg.get("cache_dir", "outputs/feature_cache")
    device = experiment_cfg.get("device", "cuda")
    batch_size = int(backbone_cfg.get("batch_size", 8))
    return backbone_name, image_size, cache_dir, device, batch_size


def get_patch_features(config: dict, records: list, cache_name: str, seed: int, cache_seed: int | None = None) -> np.ndarray:
    from src.backbones.dinov2 import build_backbone

    backbone_name, image_size, cache_dir, device, batch_size = feature_settings(config)
    batch = load_feature_cache_if_present(records, cache_dir, cache_name, seed, backbone_name, image_size, cache_seed=cache_seed)
    if batch is None:
        backbone = build_backbone(backbone_name, device=device, image_size=image_size, batch_size=batch_size)
        batch = encode_with_cache(backbone, records, cache_dir, cache_name, seed, backbone_name, image_size, cache_seed=cache_seed)
    return batch.patch_features


def fit_source_calibrator(base_config: dict, k: int, seed: int, max_classes: int | None = None) -> VectorPlattScaler:
    xs = []
    ys = []
    classes = MVTEC_CLASSES[:max_classes]
    for cls in classes:
        cfg = dict(base_config)
        cfg["dataset"] = {**base_config.get("dataset", {}), "name": "mvtec", "root": "data/mvtec", "classes": [cls]}
        cfg["model"] = {**base_config.get("model", {}), "variant": "calib_subspace_head"}
        records = load_records("mvtec", "data/mvtec", [cls])
        support = few_shot_support(records, k=k, seed=seed)
        backbone_name, _, _, _, _ = feature_settings(cfg)
        support_features = get_patch_features(cfg, support, f"mvtec_transfer_source_{cls}_{backbone_name}_k{k}_seed{seed}", seed)
        model = build_model(
            "calib_subspace_head",
            support_features,
            {**cfg.get("model", {}), "device": cfg.get("experiment", {}).get("device", "cuda")},
            seed=seed,
        )
        support_vec = model.calibration_features(support_features)
        synth_vec = model.synthetic_calibration_features(
            support_features,
            seed=seed,
            ratio=float(cfg.get("model", {}).get("synthetic_anomaly_ratio", 1.0)),
        )
        xs.append(np.concatenate([support_vec, synth_vec], axis=0))
        ys.append(np.concatenate([np.zeros(len(support_vec), dtype=np.float32), np.ones(len(synth_vec), dtype=np.float32)]))
    return VectorPlattScaler().fit(np.concatenate(xs, axis=0), np.concatenate(ys, axis=0), positive_indices=(0,))


def eval_target(base_config: dict, calibrator: VectorPlattScaler, cls: str, k: int, seed: int) -> dict:
    cfg = dict(base_config)
    cfg["dataset"] = {**base_config.get("dataset", {}), "name": "visa", "root": "data/visa", "classes": [cls]}
    cfg["model"] = {**base_config.get("model", {}), "variant": "calib_subspace_head"}
    records = load_records("visa", "data/visa", [cls])
    support = few_shot_support(records, k=k, seed=seed)
    eval_recs = evaluation_records(records)
    backbone_name, _, _, _, _ = feature_settings(cfg)
    support_features = get_patch_features(cfg, support, f"visa_transfer_support_{cls}_{backbone_name}_k{k}_seed{seed}", seed)
    eval_features = get_patch_features(cfg, eval_recs, f"visa_transfer_eval_{cls}_{backbone_name}", seed, cache_seed=0)
    model = build_model(
        "calib_subspace_head",
        support_features,
        {**cfg.get("model", {}), "device": cfg.get("experiment", {}).get("device", "cuda")},
        seed=seed,
    )
    raw_scores, _ = model.score_images(eval_features)
    labels = np.asarray([r.label for r in eval_recs], dtype=np.int64)
    probs = calibrator.predict_proba(model.calibration_features(eval_features))
    metrics = summarize_binary(labels, raw_scores, probs, bins=int(cfg.get("calibration", {}).get("bins", 15)))
    return {
        "dataset": "visa",
        "source_dataset": "mvtec",
        "class": cls,
        "k_shot": k,
        "seed": seed,
        "calibration_mode": "mvtec_transfer_normal_synthetic",
        "entropy_mean": float(entropy_binary(probs).mean()),
        **metrics,
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


def summarize(rows: list[dict]) -> list[dict]:
    from collections import defaultdict
    from statistics import mean, stdev

    groups = defaultdict(list)
    for r in rows:
        groups[(r["dataset"], int(r["k_shot"]), r["calibration_mode"])].append(r)
    out = []
    for (dataset, k, mode), g in sorted(groups.items()):
        base = {"dataset": dataset, "k_shot": k, "calibration_mode": mode, "n": len(g)}
        for m in ["auroc", "ap", "max_f1", "ece", "brier", "nll", "entropy_mean"]:
            vals = [float(r[m]) for r in g if not np.isnan(float(r[m]))]
            base[f"{m}_mean"] = mean(vals) if vals else float("nan")
            base[f"{m}_std"] = stdev(vals) if len(vals) > 1 else 0.0
        out.append(base)
    return out


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--base-config", default="configs/generated/mvtec_full/calib_subspace_head_mvtec_bottle_k1_seed0.yaml")
    parser.add_argument("--k-shots", nargs="*", type=int, default=[1, 2, 4, 8])
    parser.add_argument("--seeds", nargs="*", type=int, default=[0, 1, 2, 3, 4])
    parser.add_argument("--classes", nargs="*", default=VISA_CLASSES)
    parser.add_argument("--source-max-classes", type=int, default=None)
    parser.add_argument("--out-dir", default="outputs/paper_tables")
    parser.add_argument("--limit", type=int, default=None)
    parser.add_argument("--resume", action="store_true")
    args = parser.parse_args()
    base = load_config(args.base_config)
    out = Path(args.out_dir)
    out.mkdir(parents=True, exist_ok=True)
    lock_file = (out / "mvtec_to_visa_transfer.lock").open("w", encoding="utf-8")
    try:
        fcntl.flock(lock_file, fcntl.LOCK_EX | fcntl.LOCK_NB)
    except BlockingIOError:
        print("transfer_lock_busy: another evaluate_transfer process is running", flush=True)
        return 2
    detail_path = out / "mvtec_to_visa_transfer_detailed.csv"
    rows = read_existing(detail_path) if args.resume else []
    done = {(r["class"], int(r["k_shot"]), int(r["seed"])) for r in rows}
    count = len(rows)
    total = len(args.k_shots) * len(args.seeds) * len(args.classes)
    for k in args.k_shots:
        for seed in args.seeds:
            pending = [cls for cls in args.classes if (cls, k, seed) not in done]
            if not pending:
                continue
            calibrator = fit_source_calibrator(base, k, seed, max_classes=args.source_max_classes)
            for cls in pending:
                rows.append(eval_target(base, calibrator, cls, k, seed))
                count += 1
                done.add((cls, k, seed))
                write_csv(detail_path, rows)
                write_csv(out / "mvtec_to_visa_transfer_summary.csv", summarize(rows))
                print(f"transfer_progress={count}/{total} k={k} seed={seed} class={cls}", flush=True)
                if args.limit and count >= args.limit:
                    return 0
    print(f"runs={len(rows)}")
    print(out / "mvtec_to_visa_transfer_summary.csv")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
