# Run ablation_alpha_0p5_mvtec_carpet_k4_seed3_head_pca_k4_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p5_mvtec_carpet_k4_seed3.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.994427127430207`
- `auroc`: `0.9819422150882825`
- `brier`: `0.17714762704857306`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.33677799095455396`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.00216002077755765`
- `max_f1`: `0.9666666666666667`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.54427610060624`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_alpha_0p5_mvtec_carpet_k4_seed3_head_pca_k4_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
