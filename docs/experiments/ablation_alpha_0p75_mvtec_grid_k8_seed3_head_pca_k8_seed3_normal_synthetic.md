# Run ablation_alpha_0p75_mvtec_grid_k8_seed3_head_pca_k8_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p75_mvtec_grid_k8_seed3.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9983291562238931`
- `auroc`: `0.9949874686716792`
- `brier`: `0.1811712474111677`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.12776791743743116`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.004057048724438899`
- `max_f1`: `0.9911504424778761`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.5472282523958519`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_alpha_0p75_mvtec_grid_k8_seed3_head_pca_k8_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
