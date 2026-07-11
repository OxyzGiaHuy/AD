# Run head_pca_mvtec_grid_k8_seed4_head_pca_k8_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/head_pca_mvtec_grid_k8_seed4.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.999697519661222`
- `auroc`: `0.9991645781119465`
- `brier`: `0.27113409528161536`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.4428609021199055`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0016260252167017031`
- `max_f1`: `0.991304347826087`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.735219332277203`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/head_pca_mvtec_grid_k8_seed4_head_pca_k8_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
