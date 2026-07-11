# Run ablation_pca128_mvtec_metal_nut_k4_seed0_calib_subspace_head_k4_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca128_mvtec_metal_nut_k4_seed0.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9972324461925846`
- `auroc`: `0.987781036168133`
- `brier`: `0.10829857054859003`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.12647533300130268`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.002646295127013455`
- `max_f1`: `0.9723756906077348`
- `model_storage_mb`: `0.5659370422363281`
- `nll`: `0.5156520029243064`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_pca128_mvtec_metal_nut_k4_seed0_calib_subspace_head_k4_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
