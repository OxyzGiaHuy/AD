from __future__ import annotations

import argparse
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from src.backbones.dinov2 import build_backbone
from src.config import load_config
from src.data.datasets import load_records
from src.data.sampling import evaluation_records, few_shot_support, split_calibration
from src.run_experiment import encode_with_cache, load_feature_cache_if_present


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--run-list", required=True)
    parser.add_argument("--variant", default=None)
    parser.add_argument("--include-calib", action="store_true")
    args = parser.parse_args()

    selected = []
    seen = set()
    for raw in Path(args.run_list).read_text(encoding="utf-8").splitlines():
        if not raw.strip():
            continue
        cfg_path = Path(raw.strip())
        if args.variant and not cfg_path.name.startswith(f"{args.variant}_"):
            continue
        cfg = load_config(cfg_path)
        dataset_cfg = cfg.get("dataset", {})
        backbone_cfg = cfg.get("backbone", {})
        experiment_cfg = cfg.get("experiment", {})
        key = (
            dataset_cfg.get("name", "dataset"),
            tuple(dataset_cfg.get("classes", ["all"])),
            int(dataset_cfg.get("k_shots", [1])[0]),
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
            selected.append((cfg_path, cfg))
    if not selected:
        print("No configs selected")
        return 1

    first = selected[0][1]
    first_dataset = first.get("dataset", {})
    first_backbone = first.get("backbone", {})
    first_experiment = first.get("experiment", {})
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
    for cfg_path, cfg in selected:
        dataset_cfg = cfg.get("dataset", {})
        backbone_cfg = cfg.get("backbone", {})
        dataset_name = dataset_cfg.get("name", "dataset")
        classes = dataset_cfg.get("classes", ["all"])
        k = int(dataset_cfg.get("k_shots", [1])[0])
        seed = int(dataset_cfg.get("seeds", [0])[0])
        cache_dir = backbone_cfg.get("cache_dir", "outputs/feature_cache")
        records = load_records(dataset_name, dataset_cfg.get("root"), classes)
        support = few_shot_support(records, k=k, seed=seed)
        eval_clean = evaluation_records(records)
        jobs = [
            (support, f"{dataset_name}_support_{backbone_name}_k{k}_seed{seed}", seed, None, "support"),
            (eval_clean, f"{dataset_name}_eval_{backbone_name}", seed, 0 if backbone_name.startswith("dinov2") else seed, "eval"),
        ]
        if args.include_calib:
            calib_records, _ = split_calibration(records, seed=seed)
            if calib_records:
                jobs.append((calib_records, f"{dataset_name}_calib_{backbone_name}_seed{seed}", seed, None, "calib"))
        for records_to_encode, cache_name, record_seed, cache_seed, label in jobs:
            cached = load_feature_cache_if_present(
                records_to_encode,
                cache_dir,
                cache_name,
                record_seed,
                backbone_name,
                image_size,
                cache_seed=cache_seed,
            )
            if cached is not None:
                skipped += 1
                continue
            print(f"ENCODE {cfg_path} {label}", flush=True)
            encode_with_cache(
                backbone,
                records_to_encode,
                cache_dir,
                cache_name,
                record_seed,
                backbone_name,
                image_size,
                cache_seed=cache_seed,
            )
            completed += 1
    print(f"precompute_clean_completed={completed} skipped={skipped}", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
