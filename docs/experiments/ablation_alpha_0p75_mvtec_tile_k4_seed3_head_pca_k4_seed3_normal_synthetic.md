# Run ablation_alpha_0p75_mvtec_tile_k4_seed3_head_pca_k4_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p75_mvtec_tile_k4_seed3.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.993179723526079`
- `auroc`: `0.9841269841269841`
- `brier`: `0.18917456551490056`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.23460826354149067`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0024905997272740062`
- `max_f1`: `0.9764705882352941`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.565391502110392`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_alpha_0p75_mvtec_tile_k4_seed3_head_pca_k4_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
