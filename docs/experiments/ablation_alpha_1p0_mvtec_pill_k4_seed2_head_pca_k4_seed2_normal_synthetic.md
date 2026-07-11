# Run ablation_alpha_1p0_mvtec_pill_k4_seed2_head_pca_k4_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_1p0_mvtec_pill_k4_seed2.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9724527034193556`
- `auroc`: `0.8949809056192035`
- `brier`: `0.14104959594322317`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.14624146858375225`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.002597090091087861`
- `max_f1`: `0.9556313993174061`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.4615728012640255`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_alpha_1p0_mvtec_pill_k4_seed2_head_pca_k4_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
