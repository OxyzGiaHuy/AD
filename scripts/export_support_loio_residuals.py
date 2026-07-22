from __future__ import annotations

import argparse
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.export_sw_cad_image_views import get_features, read_existing, write_csv
from scripts.generate_benchmark_grid import MVTEC_CLASSES, VISA_CLASSES
from src.config import load_config
from src.conformal import loio_calibration
from src.data.datasets import load_records
from src.data.sampling import few_shot_support


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--base-config", default="configs/generated/visa_full/calib_subspace_head_visa_candle_k1_seed0.yaml")
    parser.add_argument("--dataset", choices=["mvtec", "visa", "mpdd"], required=True)
    parser.add_argument("--classes", nargs="*", default=None)
    parser.add_argument("--k-shots", nargs="*", type=int, default=[4, 8])
    parser.add_argument("--seeds", nargs="*", type=int, default=[0, 1, 2])
    parser.add_argument("--rho", type=float, default=0.01)
    parser.add_argument("--out", required=True)
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
    rows = read_existing(out) if args.resume else []
    done = {(row["class"], int(row["k_shot"]), int(row["seed"])) for row in rows}

    for cls in classes:
        records = load_records(args.dataset, f"data/{args.dataset}", [cls])
        for k in args.k_shots:
            for seed in args.seeds:
                key = (cls, k, seed)
                if key in done:
                    continue
                support = few_shot_support(records, k=k, seed=seed)
                support_features = get_features(config, support, f"{args.dataset}_support_{backbone}_k{k}_seed{seed}", seed)
                calibration = loio_calibration(support_features, components, rho=args.rho)
                for index, score in enumerate(calibration.image_scores):
                    rows.append({
                        "dataset": args.dataset,
                        "class": cls,
                        "k_shot": k,
                        "seed": seed,
                        "support_calibration_mode": calibration.mode,
                        "residual_index": index,
                        "loio_residual": float(score),
                    })
                done.add(key)
                write_csv(out, rows)
                print(f"support_loio_progress class={cls} k={k} seed={seed}", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
