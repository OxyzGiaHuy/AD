# Run ablation_alpha_0p25_mvtec_screw_k4_seed2_head_pca_k4_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p25_mvtec_screw_k4_seed2.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.8974584050136362`
- `auroc`: `0.775158844025415`
- `brier`: `0.2204728572324627`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.2201332848519087`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0040140139288268985`
- `max_f1`: `0.8863636363636364`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6337465418883862`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_alpha_0p25_mvtec_screw_k4_seed2_head_pca_k4_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
