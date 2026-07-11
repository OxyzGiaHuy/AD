# Run ablation_alpha_0p25_mvtec_leather_k1_seed1_head_pca_k1_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p25_mvtec_leather_k1_seed1.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `1.0`
- `auroc`: `1.0`
- `brier`: `0.21668598888442442`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.42075847281563666`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.002126819994901457`
- `max_f1`: `1.0`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.626177414222993`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_alpha_0p25_mvtec_leather_k1_seed1_head_pca_k1_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
