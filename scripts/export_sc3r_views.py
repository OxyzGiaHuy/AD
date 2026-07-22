from __future__ import annotations

import argparse
from pathlib import Path
import sys

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.evaluate_corruptions import corrupt_records, stratified_sample_records
from scripts.export_support_calibration_stats import robust_stats
from scripts.export_sw_cad_image_views import get_features, read_existing, write_csv
from scripts.generate_benchmark_grid import MVTEC_CLASSES, VISA_CLASSES
from src.config import load_config
from src.conformal import loio_calibration, top_fraction_score
from src.data.datasets import load_records
from src.data.sampling import evaluation_records, few_shot_support
from src.models.pca import PCASubspace


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--base-config", default="configs/generated/visa_full/calib_subspace_head_visa_candle_k1_seed0.yaml")
    parser.add_argument("--dataset", choices=["mvtec", "visa", "mpdd"], required=True)
    parser.add_argument("--classes", nargs="*", default=None)
    parser.add_argument("--k-shots", nargs="*", type=int, default=[4, 8])
    parser.add_argument("--seeds", nargs="*", type=int, default=[0, 1, 2])
    parser.add_argument("--corruptions", nargs="*", default=["clean", "gaussian_noise", "blur", "brightness_contrast", "jpeg"])
    parser.add_argument("--max-images", type=int, default=120)
    parser.add_argument("--tmp-root", default="/tmp/AD-sc3r")
    parser.add_argument("--rho", type=float, default=0.01)
    parser.add_argument("--out", required=True)
    parser.add_argument("--support-out", required=True)
    parser.add_argument("--support-manifest-out", default=None)
    parser.add_argument("--resume", action="store_true")
    args = parser.parse_args()

    config = load_config(args.base_config)
    if args.classes:
        classes = args.classes
    elif args.dataset == "mvtec":
        classes = MVTEC_CLASSES
    elif args.dataset == "visa":
        classes = VISA_CLASSES
    else:
        raise ValueError("MPDD classes must be passed explicitly after auditing the downloaded archive.")
    backbone = config.get("backbone", {}).get("name", "dinov2_vits14")
    components = int(config.get("model", {}).get("pca_components", 64))
    out = Path(args.out)
    support_out = Path(args.support_out)
    support_manifest_out = Path(args.support_manifest_out) if args.support_manifest_out else support_out.with_name(f"{support_out.stem}_manifest.csv")
    rows = read_existing(out) if args.resume else []
    support_rows = read_existing(support_out) if args.resume else []
    support_manifest_rows = read_existing(support_manifest_out) if args.resume else []
    done = {(row["class"], int(row["k_shot"]), int(row["seed"]), row["corruption"]) for row in rows}
    support_done = {(row["class"], int(row["k_shot"]), int(row["seed"])) for row in support_rows}
    support_manifest_done = {
        (row["class"], int(row["k_shot"]), int(row["seed"])) for row in support_manifest_rows
    }

    for cls in classes:
        records = load_records(args.dataset, f"data/{args.dataset}", [cls])
        clean_records = evaluation_records(records)
        for k in args.k_shots:
            for seed in args.seeds:
                support = few_shot_support(records, k=k, seed=seed)
                support_key = (cls, k, seed)
                if support_key not in support_manifest_done:
                    for support_index, record in enumerate(support):
                        support_manifest_rows.append({
                            "dataset": args.dataset,
                            "class": cls,
                            "k_shot": k,
                            "seed": seed,
                            "support_index": support_index,
                            "image_path": str(record.path),
                        })
                    support_manifest_done.add(support_key)
                    write_csv(support_manifest_out, support_manifest_rows)
                support_features = get_features(config, support, f"{args.dataset}_support_{backbone}_k{k}_seed{seed}", seed)
                pca = PCASubspace.fit(support_features, components)
                if support_key not in support_done:
                    calibration = loio_calibration(support_features, components, rho=args.rho)
                    support_rows.append({
                        "dataset": args.dataset,
                        "class": cls,
                        "k_shot": k,
                        "seed": seed,
                        "support_calibration_mode": calibration.mode,
                        **robust_stats(calibration.image_scores),
                    })
                    support_done.add(support_key)
                    write_csv(support_out, support_rows)
                for corruption in args.corruptions:
                    key = (cls, k, seed, corruption)
                    if key in done:
                        continue
                    selected = corrupt_records(
                        clean_records,
                        corruption,
                        Path(args.tmp_root) / args.dataset / cls / f"seed{seed}" / corruption,
                        seed=seed,
                        max_images=args.max_images,
                    )
                    base_selected = stratified_sample_records(clean_records, args.max_images, seed)
                    if len(base_selected) != len(selected):
                        raise RuntimeError("Corrupted and base-image manifests have different lengths.")
                    features = get_features(
                        config,
                        selected,
                        f"{args.dataset}_sc3r_{cls}_{corruption}_{backbone}_seed{seed}_n{args.max_images}",
                        seed,
                        cache_seed=0 if backbone.startswith("dinov2") else seed,
                    )
                    raw_scores = top_fraction_score(pca.residual_scores(features), rho=args.rho)
                    corruption_parameters = {
                        "clean": "none",
                        "gaussian_noise": "severity=0.05",
                        "blur": "kernel=3",
                        "brightness_contrast": "brightness=0.05;contrast=1.15",
                        "jpeg": "quality=60",
                    }[corruption]
                    for record, base_record, raw_score in zip(selected, base_selected, raw_scores):
                        rows.append({
                            "dataset": args.dataset,
                            "class": cls,
                            "k_shot": k,
                            "seed": seed,
                            "corruption": corruption,
                            "image_path": str(record.path),
                            "base_image_path": str(base_record.path),
                            "label": int(record.label),
                            "raw_score": float(raw_score),
                            "sampling_protocol": "label_stratified_random",
                            "sampling_seed": seed,
                            "max_images": args.max_images,
                            "corruption_parameters": corruption_parameters,
                        })
                    done.add(key)
                    write_csv(out, rows)
                    print(f"sc3r_progress class={cls} k={k} seed={seed} corruption={corruption}", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
