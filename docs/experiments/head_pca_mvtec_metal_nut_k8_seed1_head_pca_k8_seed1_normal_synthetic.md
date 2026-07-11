# Run head_pca_mvtec_metal_nut_k8_seed1_head_pca_k8_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/head_pca_mvtec_metal_nut_k8_seed1.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.992689452080543`
- `auroc`: `0.9711632453567938`
- `brier`: `0.24689771981955455`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.3969062802584274`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.001598508186314417`
- `max_f1`: `0.9633507853403142`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6869275379988794`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/head_pca_mvtec_metal_nut_k8_seed1_head_pca_k8_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
