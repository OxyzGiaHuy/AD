# Run ablation_alpha_1p0_mvtec_transistor_k1_seed3_head_pca_k1_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_1p0_mvtec_transistor_k1_seed3.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.6409159048891138`
- `auroc`: `0.7120833333333333`
- `brier`: `0.3423251246168486`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.3228919124603271`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.002846057265996933`
- `max_f1`: `0.6495726495726496`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.8951737267061161`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_alpha_1p0_mvtec_transistor_k1_seed3_head_pca_k1_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
