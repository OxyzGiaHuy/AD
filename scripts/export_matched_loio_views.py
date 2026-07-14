from __future__ import annotations

import argparse
from pathlib import Path
import sys

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.evaluate_corruptions import corrupt_records
from scripts.export_sw_cad_image_views import get_features, read_existing, write_csv
from scripts.generate_benchmark_grid import MVTEC_CLASSES, VISA_CLASSES
from src.config import load_config
from src.conformal import conformal_p_values, loio_calibration, matched_loio_image_p_values, top_fraction_score
from src.data.datasets import load_records
from src.data.sampling import evaluation_records, few_shot_support
from src.models.pca import PCASubspace


def evaluate_case(config: dict, dataset: str, cls: str, k: int, seed: int, corruption: str,
                  max_images: int | None, tmp_root: str, rho: float) -> list[dict]:
    cfg = dict(config)
    cfg["dataset"] = {
        **config.get("dataset", {}),
        "name": dataset,
        "root": f"data/{dataset}",
        "classes": [cls],
        "k_shots": [k],
        "seeds": [seed],
    }
    backbone = cfg.get("backbone", {}).get("name", "dinov2_vits14")
    components = int(cfg.get("model", {}).get("pca_components", 64))
    records = load_records(dataset, f"data/{dataset}", [cls])
    support = few_shot_support(records, k=k, seed=seed)
    clean = evaluation_records(records)
    selected = corrupt_records(
        clean,
        corruption,
        Path(tmp_root) / dataset / cls / f"seed{seed}" / corruption,
        seed=seed,
        max_images=max_images,
    )
    support_features = get_features(
        cfg, support, f"{dataset}_support_{backbone}_k{k}_seed{seed}", seed
    )
    test_features = get_features(
        cfg,
        selected,
        f"{dataset}_corrupt_{cls}_{corruption}_{backbone}_seed{seed}",
        seed,
        cache_seed=0 if backbone.startswith("dinov2") else seed,
    )

    full_pca = PCASubspace.fit(support_features, components)
    raw_score = top_fraction_score(full_pca.residual_scores(test_features), rho=rho)
    matched = matched_loio_image_p_values(support_features, test_features, components, rho=rho)
    legacy_p = conformal_p_values(matched.calibration_scores, raw_score)

    rows = []
    for rec, score, p_matched, p_legacy in zip(selected, raw_score, matched.p_values, legacy_p):
        rows.append({
            "dataset": dataset,
            "class": cls,
            "k_shot": k,
            "seed": seed,
            "corruption": corruption,
            "image_path": str(rec.path),
            "label": int(rec.label),
            "raw_score": float(score),
            "image_p_loio": float(p_matched),
            "image_p_loio_legacy": float(p_legacy),
            "conformal_prob_loio": float(1.0 - p_matched),
            "conformal_prob_loio_legacy": float(1.0 - p_legacy),
            "loio_protocol": "fold_matched",
            "attainable_alpha": float(matched.attainable_alpha),
        })
    return rows


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--base-config", default="configs/generated/visa_full/calib_subspace_head_visa_candle_k1_seed0.yaml")
    parser.add_argument("--dataset", choices=["visa", "mvtec"], required=True)
    parser.add_argument("--classes", nargs="*", default=None)
    parser.add_argument("--k-shots", nargs="*", type=int, default=[4, 8])
    parser.add_argument("--seeds", nargs="*", type=int, default=[0, 1, 2, 3, 4])
    parser.add_argument("--corruptions", nargs="*", default=["clean", "gaussian_noise", "blur", "brightness_contrast", "jpeg"])
    parser.add_argument("--max-images", type=int, default=None)
    parser.add_argument("--tmp-root", default="/home/crl/AD/tmp/matched_loio")
    parser.add_argument("--out-dir", default="outputs/paper_tables")
    parser.add_argument("--run-tag", default="matched_loio")
    parser.add_argument("--rho", type=float, default=0.01)
    parser.add_argument("--resume", action="store_true")
    args = parser.parse_args()

    config = load_config(args.base_config)
    all_classes = VISA_CLASSES if args.dataset == "visa" else MVTEC_CLASSES
    classes = args.classes or all_classes
    out = Path(args.out_dir) / f"matched_loio_views_{args.run_tag}.csv"
    rows = read_existing(out) if args.resume else []
    done = {
        (r["dataset"], r["class"], int(r["k_shot"]), int(r["seed"]), r["corruption"])
        for r in rows
    }
    jobs = [
        (cls, k, seed, corruption)
        for cls in classes
        for k in args.k_shots
        for seed in args.seeds
        for corruption in args.corruptions
    ]
    for cls, k, seed, corruption in jobs:
        key = (args.dataset, cls, k, seed, corruption)
        if key in done:
            continue
        rows.extend(evaluate_case(
            config, args.dataset, cls, k, seed, corruption, args.max_images, args.tmp_root, args.rho
        ))
        done.add(key)
        write_csv(out, rows)
        print(
            f"matched_loio_progress={len(done)}/{len(jobs)} dataset={args.dataset} "
            f"class={cls} k={k} seed={seed} corruption={corruption}",
            flush=True,
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
