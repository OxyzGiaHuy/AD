from __future__ import annotations

import argparse
from pathlib import Path
import sys

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.evaluate_corruptions import corrupt_records
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
    parser.add_argument("--dataset", choices=["mvtec", "visa"], required=True)
    parser.add_argument("--classes", nargs="*", default=None)
    parser.add_argument("--k-shots", nargs="*", type=int, default=[4, 8])
    parser.add_argument("--seeds", nargs="*", type=int, default=[0, 1, 2])
    parser.add_argument("--corruptions", nargs="*", default=["clean", "gaussian_noise", "blur", "brightness_contrast", "jpeg"])
    parser.add_argument("--max-images", type=int, default=120)
    parser.add_argument("--tmp-root", default="/home/crl/AD/tmp/sc3r")
    parser.add_argument("--rho", type=float, default=0.01)
    parser.add_argument("--out", required=True)
    parser.add_argument("--support-out", required=True)
    parser.add_argument("--resume", action="store_true")
    args = parser.parse_args()

    config = load_config(args.base_config)
    classes = args.classes or (MVTEC_CLASSES if args.dataset == "mvtec" else VISA_CLASSES)
    backbone = config.get("backbone", {}).get("name", "dinov2_vits14")
    components = int(config.get("model", {}).get("pca_components", 64))
    out = Path(args.out)
    support_out = Path(args.support_out)
    rows = read_existing(out) if args.resume else []
    support_rows = read_existing(support_out) if args.resume else []
    done = {(row["class"], int(row["k_shot"]), int(row["seed"]), row["corruption"]) for row in rows}
    support_done = {(row["class"], int(row["k_shot"]), int(row["seed"])) for row in support_rows}

    for cls in classes:
        records = load_records(args.dataset, f"data/{args.dataset}", [cls])
        clean_records = evaluation_records(records)
        for k in args.k_shots:
            for seed in args.seeds:
                support = few_shot_support(records, k=k, seed=seed)
                support_features = get_features(config, support, f"{args.dataset}_support_{backbone}_k{k}_seed{seed}", seed)
                pca = PCASubspace.fit(support_features, components)
                support_key = (cls, k, seed)
                if support_key not in support_done:
                    calibration = loio_calibration(support_features, components, rho=args.rho)
                    support_rows.append({
                        "dataset": args.dataset,
                        "class": cls,
                        "k_shot": k,
                        "seed": seed,
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
                    features = get_features(
                        config,
                        selected,
                        f"{args.dataset}_sc3r_{cls}_{corruption}_{backbone}_seed{seed}_n{args.max_images}",
                        seed,
                        cache_seed=0 if backbone.startswith("dinov2") else seed,
                    )
                    raw_scores = top_fraction_score(pca.residual_scores(features), rho=args.rho)
                    for record, raw_score in zip(selected, raw_scores):
                        rows.append({
                            "dataset": args.dataset,
                            "class": cls,
                            "k_shot": k,
                            "seed": seed,
                            "corruption": corruption,
                            "image_path": str(record.path),
                            "label": int(record.label),
                            "raw_score": float(raw_score),
                            "sampling_protocol": "label_stratified_random",
                            "sampling_seed": seed,
                            "max_images": args.max_images,
                        })
                    done.add(key)
                    write_csv(out, rows)
                    print(f"sc3r_progress class={cls} k={k} seed={seed} corruption={corruption}", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
