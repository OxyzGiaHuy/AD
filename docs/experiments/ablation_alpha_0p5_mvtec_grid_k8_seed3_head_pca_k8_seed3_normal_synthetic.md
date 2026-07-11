# Run ablation_alpha_0p5_mvtec_grid_k8_seed3_head_pca_k8_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p5_mvtec_grid_k8_seed3.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9994052928932501`
- `auroc`: `0.9983291562238931`
- `brier`: `0.19224063322951132`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.3822216269297477`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.00469153634726237`
- `max_f1`: `0.9911504424778761`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.574873149406668`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_alpha_0p5_mvtec_grid_k8_seed3_head_pca_k8_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
