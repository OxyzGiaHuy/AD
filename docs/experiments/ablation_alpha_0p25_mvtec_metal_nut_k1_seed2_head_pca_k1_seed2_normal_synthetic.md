# Run ablation_alpha_0p25_mvtec_metal_nut_k1_seed2_head_pca_k1_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p25_mvtec_metal_nut_k1_seed2.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9925422554560008`
- `auroc`: `0.969208211143695`
- `brier`: `0.2131827325372708`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.270405459922293`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.002766114959250326`
- `max_f1`: `0.9621621621621622`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6191216172028255`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_alpha_0p25_mvtec_metal_nut_k1_seed2_head_pca_k1_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
