# Run ablation_alpha_1p0_mvtec_bottle_k8_seed3_head_pca_k8_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_1p0_mvtec_bottle_k8_seed3.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9941519612585865`
- `auroc`: `0.9809523809523809`
- `brier`: `0.16625968204776256`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.12965714787862392`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.002846314897199711`
- `max_f1`: `0.9612403100775194`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.514449549569353`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_alpha_1p0_mvtec_bottle_k8_seed3_head_pca_k8_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
