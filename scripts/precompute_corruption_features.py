
from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import numpy as np

from scripts.evaluate_corruptions import CORRUPTION_FUNCS, corrupt_records, load_feature_cache_if_present
from src.backbones.dinov2 import build_backbone
from src.config import load_config
from src.data.datasets import load_records
from src.data.sampling import evaluation_records
from src.run_experiment import encode_with_cache


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--run-list", default="configs/generated/mvtec_full/run_list.txt")
    parser.add_argument("--variant", default="calib_subspace_head")
    parser.add_argument("--tmp-root", default="/tmp/AD-corruptions")
    args = parser.parse_args()

    configs = []
    seen = set()
    for raw in Path(args.run_list).read_text(encoding="utf-8").splitlines():
        if not raw.strip():
            continue
        cfg_path = Path(raw.strip())
        if not cfg_path.name.startswith(f"{args.variant}_"):
            continue
        cfg = load_config(cfg_path)
        dataset_cfg = cfg.get("dataset", {})
        backbone_cfg = cfg.get("backbone", {})
        experiment_cfg = cfg.get("experiment", {})
        key = (
            dataset_cfg.get("name", "mvtec"),
            tuple(dataset_cfg.get("classes", ["all"])),
            int(dataset_cfg.get("seeds", [0])[0]),
            int(dataset_cfg.get("image_size", backbone_cfg.get("image_size", 518))),
            backbone_cfg.get("name", "identity_patch"),
            backbone_cfg.get("cache_dir", "outputs/feature_cache"),
            dataset_cfg.get("root"),
            experiment_cfg.get("device", "cuda"),
            int(backbone_cfg.get("batch_size", 8)),
        )
        if key not in seen:
            seen.add(key)
            configs.append((cfg_path, cfg, key))

    if not configs:
        print("No configs selected")
        return 1

    first_cfg = configs[0][1]
    first_dataset = first_cfg.get("dataset", {})
    first_backbone = first_cfg.get("backbone", {})
    first_experiment = first_cfg.get("experiment", {})
    backbone_name = first_backbone.get("name", "identity_patch")
    image_size = int(first_dataset.get("image_size", first_backbone.get("image_size", 518)))
    backbone = build_backbone(
        backbone_name,
        device=first_experiment.get("device", "cuda"),
        image_size=image_size,
        batch_size=int(first_backbone.get("batch_size", 8)),
    )

    completed = 0
    skipped = 0
    for cfg_path, cfg, _ in configs:
        dataset_cfg = cfg.get("dataset", {})
        backbone_cfg = cfg.get("backbone", {})
        dataset_name = dataset_cfg.get("name", "dataset")
        cache_dir = backbone_cfg.get("cache_dir", "outputs/feature_cache")
        classes = dataset_cfg.get("classes", ["all"])
        class_key = "-".join(classes) if isinstance(classes, list) else str(classes)
        seed = int(dataset_cfg.get("seeds", [0])[0])
        records = load_records(dataset_name, dataset_cfg.get("root"), classes)
        eval_clean = evaluation_records(records)
        for corruption in CORRUPTION_FUNCS:
            tmp_dir = Path(args.tmp_root) / dataset_name / class_key / f"seed{seed}" / corruption
            eval_corrupt = corrupt_records(eval_clean, corruption, tmp_dir, seed=seed, max_images=None)
            cache_name = f"{dataset_name}_corrupt_{class_key}_{corruption}_{backbone_name}_seed{seed}"
            cache_seed = 0 if backbone_name.startswith("dinov2") else seed
            cached = load_feature_cache_if_present(
                eval_corrupt,
                cache_dir,
                cache_name,
                seed,
                backbone_name,
                image_size,
                cache_seed=cache_seed,
            )
            if cached is not None:
                skipped += 1
                print(f"SKIP {cfg_path} {corruption}", flush=True)
                continue
            print(f"ENCODE {cfg_path} {corruption}", flush=True)
            encode_with_cache(
                backbone,
                eval_corrupt,
                cache_dir,
                cache_name,
                seed,
                backbone_name,
                image_size,
                cache_seed=cache_seed,
            )
            completed += 1
    print(f"precompute_completed={completed} skipped={skipped}", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
