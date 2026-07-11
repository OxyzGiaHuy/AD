from __future__ import annotations

import argparse
from pathlib import Path

import numpy as np

from .backbones.dinov2 import build_backbone, cache_path
from .data.datasets import load_records
from .data.sampling import few_shot_support
from .utils.io import ensure_dir


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dataset", required=True, choices=["mvtec", "visa", "synthetic"])
    parser.add_argument("--root", default=None)
    parser.add_argument("--classes", nargs="*", default=["all"])
    parser.add_argument("--backbone", default="dinov2_vits14")
    parser.add_argument("--k-shot", type=int, default=4)
    parser.add_argument("--seed", type=int, default=0)
    parser.add_argument("--cache-dir", default="outputs/feature_cache")
    parser.add_argument("--device", default="cuda")
    args = parser.parse_args(argv)

    classes = "all" if args.classes == ["all"] else args.classes
    records = load_records(args.dataset, args.root, classes)
    support = few_shot_support(records, k=args.k_shot, seed=args.seed)
    backbone = build_backbone(args.backbone, device=args.device)
    features = backbone.encode_records(support, seed=args.seed)
    ensure_dir(args.cache_dir)
    categories = sorted({r.category for r in support})
    out = cache_path(args.cache_dir, args.dataset, "-".join(categories), args.backbone, args.k_shot, args.seed)
    np.savez_compressed(out, patch_features=features.patch_features, grid_size=np.asarray(features.grid_size))
    print(out)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

