# Run ablation_pca16_mvtec_bottle_k4_seed2_calib_subspace_head_k4_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca16_mvtec_bottle_k4_seed2.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9514117361036333`
- `auroc`: `0.9095238095238095`
- `brier`: `0.14083809239738743`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.16076950441641977`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.002846354237162923`
- `max_f1`: `0.9538461538461539`
- `model_storage_mb`: `0.4018745422363281`
- `nll`: `0.45391639987562465`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_pca16_mvtec_bottle_k4_seed2_calib_subspace_head_k4_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
