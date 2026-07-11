from __future__ import annotations

import argparse
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.generate_benchmark_grid import MVTEC_CLASSES


TEMPLATE = """experiment:
  name: {name}
  output_dir: outputs
  docs_dir: docs
  device: cuda
  mixed_precision: true

dataset:
  name: mvtec
  root: data/mvtec
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
  alpha: {alpha}
  pca_components: {pca_components}
  head_hidden_dim: 256
  train_steps: 500
  learning_rate: 0.001
  weight_decay: 0.0001
  batch_size: 4096
  synthetic_anomaly_ratio: 1.0

calibration:
  modes: [{calibration_mode}]
  method: {calibration_method}
  bins: 15

robustness:
  attacks:
    - name: fgsm
      epsilons: ["8/255"]
  corruptions: [gaussian_noise, blur, brightness_contrast, jpeg]
"""


def write_config(path: Path, **kwargs) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(TEMPLATE.format(**kwargs), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--out-dir", default="configs/generated/mvtec_ablations")
    parser.add_argument("--write-run-list", default="configs/generated/mvtec_ablations/run_list.txt")
    parser.add_argument("--classes", nargs="*", default=MVTEC_CLASSES)
    parser.add_argument("--k-shots", nargs="*", type=int, default=[1, 4, 8])
    parser.add_argument("--seeds", nargs="*", type=int, default=[0, 1, 2, 3, 4])
    args = parser.parse_args()

    out_dir = Path(args.out_dir)
    paths = []
    for cls in args.classes:
        for k in args.k_shots:
            for seed in args.seeds:
                for alpha_text, alpha in [("0p0", 0.0), ("0p25", 0.25), ("0p5", 0.5), ("0p75", 0.75), ("1p0", 1.0)]:
                    name = f"ablation_alpha_{alpha_text}_mvtec_{cls}_k{k}_seed{seed}"
                    path = out_dir / f"{name}.yaml"
                    write_config(
                        path,
                        name=name,
                        cls=cls,
                        k=k,
                        seed=seed,
                        variant="head_pca",
                        alpha=alpha,
                        pca_components=64,
                        calibration_mode="normal_synthetic",
                        calibration_method="platt",
                    )
                    paths.append(path)
                for pca_components in [16, 32, 64, 128]:
                    name = f"ablation_pca{pca_components}_mvtec_{cls}_k{k}_seed{seed}"
                    path = out_dir / f"{name}.yaml"
                    write_config(
                        path,
                        name=name,
                        cls=cls,
                        k=k,
                        seed=seed,
                        variant="calib_subspace_head",
                        alpha=0.0,
                        pca_components=pca_components,
                        calibration_mode="normal_synthetic",
                        calibration_method="vector_platt",
                    )
                    paths.append(path)
                name = f"ablation_calib_upper_mvtec_{cls}_k{k}_seed{seed}"
                path = out_dir / f"{name}.yaml"
                write_config(
                    path,
                    name=name,
                    cls=cls,
                    k=k,
                    seed=seed,
                    variant="calib_subspace_head",
                    alpha=0.0,
                    pca_components=64,
                    calibration_mode="normal_plus_anomaly_val",
                    calibration_method="vector_platt",
                )
                paths.append(path)
    run_list = Path(args.write_run_list)
    run_list.parent.mkdir(parents=True, exist_ok=True)
    run_list.write_text("\n".join(str(path) for path in paths) + "\n", encoding="utf-8")
    print(f"Wrote {len(paths)} ablation configs")
    print(run_list)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
