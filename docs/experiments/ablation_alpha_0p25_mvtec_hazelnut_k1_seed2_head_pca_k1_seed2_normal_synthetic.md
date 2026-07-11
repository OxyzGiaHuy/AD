# Run ablation_alpha_0p25_mvtec_hazelnut_k1_seed2_head_pca_k1_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p25_mvtec_hazelnut_k1_seed2.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9206899460256285`
- `auroc`: `0.8778571428571429`
- `brier`: `0.23707384055481984`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.15395494265989823`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0020132341845469043`
- `max_f1`: `0.8652482269503546`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6672053279278721`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_alpha_0p25_mvtec_hazelnut_k1_seed2_head_pca_k1_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
