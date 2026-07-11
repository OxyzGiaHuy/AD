# Run ablation_alpha_1p0_mvtec_tile_k4_seed3_head_pca_k4_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_1p0_mvtec_tile_k4_seed3.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9884758316799875`
- `auroc`: `0.9725829725829725`
- `brier`: `0.18936019819519817`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.11203422862240389`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0030755428040129505`
- `max_f1`: `0.9595375722543352`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.5640158972237411`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_alpha_1p0_mvtec_tile_k4_seed3_head_pca_k4_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
