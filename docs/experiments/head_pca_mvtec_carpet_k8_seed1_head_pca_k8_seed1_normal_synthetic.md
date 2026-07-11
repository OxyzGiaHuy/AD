# Run head_pca_mvtec_carpet_k8_seed1_head_pca_k8_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/head_pca_mvtec_carpet_k8_seed1.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9974594188000838`
- `auroc`: `0.9919743178170144`
- `brier`: `0.236800926712589`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.40146651201777983`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.001598293009476784`
- `max_f1`: `0.9834254143646409`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6663837514331823`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/head_pca_mvtec_carpet_k8_seed1_head_pca_k8_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
