# Run ablation_alpha_1p0_mvtec_wood_k1_seed3_head_pca_k1_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_1p0_mvtec_wood_k1_seed3.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.8875570994064041`
- `auroc`: `0.7881578947368421`
- `brier`: `0.18243960025556902`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.03394178272802628`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0022893187507421154`
- `max_f1`: `0.9090909090909091`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.5512780502981073`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_alpha_1p0_mvtec_wood_k1_seed3_head_pca_k1_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
