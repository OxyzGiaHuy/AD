from __future__ import annotations

import argparse
import csv
from pathlib import Path
import sys

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.export_sw_cad_image_views import get_features
from scripts.generate_benchmark_grid import MVTEC_CLASSES, VISA_CLASSES
from src.config import load_config
from src.conformal import loio_calibration
from src.data.datasets import load_records
from src.data.sampling import few_shot_support


def robust_stats(values: np.ndarray) -> dict[str, float]:
    scores = np.asarray(values, dtype=np.float64)
    median = float(np.median(scores))
    mad = float(np.median(np.abs(scores - median)))
    return {
        "support_cal_median": median,
        "support_cal_mad": mad,
        "support_cal_q25": float(np.quantile(scores, 0.25)),
        "support_cal_q75": float(np.quantile(scores, 0.75)),
        "support_cal_mean": float(scores.mean()),
        "support_cal_std": float(scores.std()),
        "support_cal_count": len(scores),
    }


def write_csv(path: Path, rows: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--base-config", default="configs/generated/visa_full/calib_subspace_head_visa_candle_k1_seed0.yaml")
    parser.add_argument("--dataset", choices=["mvtec", "visa"], required=True)
    parser.add_argument("--classes", nargs="*", default=None)
    parser.add_argument("--k-shots", nargs="*", type=int, default=[4, 8])
    parser.add_argument("--seeds", nargs="*", type=int, default=[0, 1, 2])
    parser.add_argument("--rho", type=float, default=0.01)
    parser.add_argument("--out", required=True)
    args = parser.parse_args()

    config = load_config(args.base_config)
    classes = args.classes or (MVTEC_CLASSES if args.dataset == "mvtec" else VISA_CLASSES)
    backbone = config.get("backbone", {}).get("name", "dinov2_vits14")
    components = int(config.get("model", {}).get("pca_components", 64))
    rows: list[dict] = []
    for cls in classes:
        records = load_records(args.dataset, f"data/{args.dataset}", [cls])
        for k in args.k_shots:
            for seed in args.seeds:
                support = few_shot_support(records, k=k, seed=seed)
                features = get_features(
                    config,
                    support,
                    f"{args.dataset}_support_{backbone}_k{k}_seed{seed}",
                    seed,
                )
                calibration = loio_calibration(features, components, rho=args.rho)
                rows.append({"dataset": args.dataset, "class": cls, "k_shot": k, "seed": seed, **robust_stats(calibration.image_scores)})
                print(f"support_stats class={cls} k={k} seed={seed}", flush=True)
    write_csv(Path(args.out), rows)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
