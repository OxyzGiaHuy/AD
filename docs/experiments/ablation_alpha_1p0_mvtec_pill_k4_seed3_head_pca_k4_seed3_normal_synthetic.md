# Run ablation_alpha_1p0_mvtec_pill_k4_seed3_head_pca_k4_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_1p0_mvtec_pill_k4_seed3.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9764954363762177`
- `auroc`: `0.9067103109656302`
- `brier`: `0.1419629803572776`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.14520551094751874`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0024523082339835025`
- `max_f1`: `0.952054794520548`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.463831650077563`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_alpha_1p0_mvtec_pill_k4_seed3_head_pca_k4_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
