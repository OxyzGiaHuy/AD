# Run ablation_alpha_0p75_mvtec_carpet_k1_seed2_head_pca_k1_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p75_mvtec_carpet_k1_seed2.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9867345568779409`
- `auroc`: `0.956661316211878`
- `brier`: `0.17888929736725265`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.20024870552568355`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0024061892977637104`
- `max_f1`: `0.9555555555555556`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.5454143874675695`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_alpha_0p75_mvtec_carpet_k1_seed2_head_pca_k1_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
