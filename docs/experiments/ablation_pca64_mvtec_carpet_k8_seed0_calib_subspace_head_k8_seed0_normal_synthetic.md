# Run ablation_pca64_mvtec_carpet_k8_seed0_calib_subspace_head_k8_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca64_mvtec_carpet_k8_seed0.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9994920791527584`
- `auroc`: `0.9983948635634029`
- `brier`: `0.0689103562878577`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.08232671524816923`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.00147760595776077`
- `max_f1`: `0.994413407821229`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `0.3011136679530358`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_pca64_mvtec_carpet_k8_seed0_calib_subspace_head_k8_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
