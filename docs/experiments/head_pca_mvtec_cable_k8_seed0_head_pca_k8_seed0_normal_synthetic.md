# Run head_pca_mvtec_cable_k8_seed0_head_pca_k8_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/head_pca_mvtec_cable_k8_seed0.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9479183332658181`
- `auroc`: `0.9002998500749625`
- `brier`: `0.24106711515577572`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.22847066382567088`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0016203316301107407`
- `max_f1`: `0.88`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6752585337825354`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/head_pca_mvtec_cable_k8_seed0_head_pca_k8_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
