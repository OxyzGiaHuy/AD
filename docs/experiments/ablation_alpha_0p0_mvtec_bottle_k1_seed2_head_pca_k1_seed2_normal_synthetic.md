# Run ablation_alpha_0p0_mvtec_bottle_k1_seed2_head_pca_k1_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p0_mvtec_bottle_k1_seed2.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9681185233245325`
- `auroc`: `0.9071428571428571`
- `brier`: `0.24996714595829142`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.2810435585946922`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0020786265517214694`
- `max_f1`: `0.9197080291970803`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6930756618367027`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_alpha_0p0_mvtec_bottle_k1_seed2_head_pca_k1_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
