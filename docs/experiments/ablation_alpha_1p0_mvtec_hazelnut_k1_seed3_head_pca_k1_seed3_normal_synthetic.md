# Run ablation_alpha_1p0_mvtec_hazelnut_k1_seed3_head_pca_k1_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_1p0_mvtec_hazelnut_k1_seed3.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.8750055147497194`
- `auroc`: `0.7339285714285714`
- `brier`: `0.23906373759591165`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.08752505074847827`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0035082040523940865`
- `max_f1`: `0.8129032258064516`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6735979149274998`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_alpha_1p0_mvtec_hazelnut_k1_seed3_head_pca_k1_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
