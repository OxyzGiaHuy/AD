# Run ablation_alpha_0p75_mvtec_metal_nut_k1_seed3_head_pca_k1_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p75_mvtec_metal_nut_k1_seed3.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9747257664766665`
- `auroc`: `0.8934506353861192`
- `brier`: `0.172376856444463`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.21927098761434138`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0017875840806442758`
- `max_f1`: `0.914572864321608`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.532439880948432`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_alpha_0p75_mvtec_metal_nut_k1_seed3_head_pca_k1_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
