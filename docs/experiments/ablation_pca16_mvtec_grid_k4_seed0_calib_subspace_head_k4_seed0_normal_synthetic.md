# Run ablation_pca16_mvtec_grid_k4_seed0_calib_subspace_head_k4_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca16_mvtec_grid_k4_seed0.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.8554435907524347`
- `auroc`: `0.6741854636591479`
- `brier`: `0.23428326197667543`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.2295657885380281`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0030107273935125424`
- `max_f1`: `0.8818897637795275`
- `model_storage_mb`: `0.4018745422363281`
- `nll`: `0.8886624693421555`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_pca16_mvtec_grid_k4_seed0_calib_subspace_head_k4_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
