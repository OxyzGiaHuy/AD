# Run ablation_alpha_0p0_mvtec_leather_k1_seed2_head_pca_k1_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p0_mvtec_leather_k1_seed2.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9980770757031461`
- `auroc`: `0.9945652173913043`
- `brier`: `0.25202330933472306`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.47838448660988964`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0026419736565120758`
- `max_f1`: `0.989247311827957`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6971419259291695`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_alpha_0p0_mvtec_leather_k1_seed2_head_pca_k1_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
