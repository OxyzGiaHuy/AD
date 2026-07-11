from __future__ import annotations

import argparse
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

MVTEC_CLASSES = [
    "bottle", "cable", "capsule", "carpet", "grid", "hazelnut", "leather", "metal_nut",
    "pill", "screw", "tile", "toothbrush", "transistor", "wood", "zipper",
]
VISA_CLASSES = [
    "candle", "capsules", "cashew", "chewinggum", "fryum", "macaroni1", "macaroni2",
    "pcb1", "pcb2", "pcb3", "pcb4", "pipe_fryum",
]
VARIANTS = ["patchcore", "anomalydino", "subspacead", "head_pca", "calib_subspace_head"]

TEMPLATE = """experiment:
  name: {name}
  output_dir: outputs
  docs_dir: docs
  device: cuda
  mixed_precision: true

dataset:
  name: {dataset}
  root: {root}
  classes: [{cls}]
  k_shots: [{k}]
  seeds: [{seed}]
  image_size: 518

backbone:
  name: dinov2_vits14
  frozen: true
  cache_dir: outputs/feature_cache
  batch_size: 8

model:
  variant: {variant}
  head_type: mlp
  alpha: 0.0
  pca_components: 64
  head_hidden_dim: 256
  train_steps: 500
  learning_rate: 0.001
  weight_decay: 0.0001
  batch_size: 4096
  synthetic_anomaly_ratio: 1.0

calibration:
  modes: [normal_synthetic]
  method: {method}
  bins: 15

robustness:
  attacks:
    - name: fgsm
      epsilons: ["8/255"]
  corruptions: [gaussian_noise, blur, brightness_contrast, jpeg]
"""


def config_text(dataset: str, cls: str, variant: str, k: int, seed: int, root: str) -> str:
    name = f"{variant}_{dataset}_{cls}_k{k}_seed{seed}"
    method = "vector_platt" if variant == "calib_subspace_head" else "platt"
    return TEMPLATE.format(name=name, dataset=dataset, root=root, cls=cls, k=k, seed=seed, variant=variant, method=method)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dataset", default="mvtec", choices=["mvtec", "visa"])
    parser.add_argument("--root", default=None)
    parser.add_argument("--out-dir", default=None)
    parser.add_argument("--classes", nargs="*", default=None)
    parser.add_argument("--k-shots", nargs="*", type=int, default=[1, 2, 4, 8])
    parser.add_argument("--seeds", nargs="*", type=int, default=[0, 1, 2, 3, 4])
    parser.add_argument("--variants", nargs="*", default=VARIANTS)
    parser.add_argument("--write-run-list", default=None)
    args = parser.parse_args()
    if args.root is None:
        args.root = f"data/{args.dataset}"
    if args.out_dir is None:
        args.out_dir = f"configs/generated/{args.dataset}_full"
    if args.write_run_list is None:
        args.write_run_list = f"configs/generated/{args.dataset}_full/run_list.txt"
    if args.classes is None:
        args.classes = MVTEC_CLASSES if args.dataset == "mvtec" else VISA_CLASSES
    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    paths = []
    for variant in args.variants:
        for cls in args.classes:
            for k in args.k_shots:
                for seed in args.seeds:
                    path = out_dir / f"{variant}_{args.dataset}_{cls}_k{k}_seed{seed}.yaml"
                    path.write_text(config_text(args.dataset, cls, variant, k, seed, args.root), encoding="utf-8")
                    paths.append(path)
    run_list = Path(args.write_run_list)
    run_list.parent.mkdir(parents=True, exist_ok=True)
    run_list.write_text("\n".join(str(p) for p in paths) + "\n", encoding="utf-8")
    print(f"Wrote {len(paths)} configs")
    print(run_list)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
