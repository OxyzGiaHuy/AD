# Run ablation_alpha_0p25_mvtec_metal_nut_k1_seed3_head_pca_k1_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p25_mvtec_metal_nut_k1_seed3.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9842046732630342`
- `auroc`: `0.9335288367546432`
- `brier`: `0.21662410915985011`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.3142715220865996`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0027969200973925385`
- `max_f1`: `0.9381443298969072`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6261045260420843`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_alpha_0p25_mvtec_metal_nut_k1_seed3_head_pca_k1_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
