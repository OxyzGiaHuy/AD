# Run ablation_alpha_0p0_mvtec_transistor_k8_seed4_head_pca_k8_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p0_mvtec_transistor_k8_seed4.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9126123146117624`
- `auroc`: `0.9316666666666666`
- `brier`: `0.2356333589878406`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.13373928189277645`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0029185969568789006`
- `max_f1`: `0.8533333333333334`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6643685569887547`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_alpha_0p0_mvtec_transistor_k8_seed4_head_pca_k8_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
