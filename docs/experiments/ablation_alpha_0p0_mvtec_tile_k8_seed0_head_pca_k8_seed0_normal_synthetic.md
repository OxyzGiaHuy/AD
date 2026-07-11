# Run ablation_alpha_0p0_mvtec_tile_k8_seed0_head_pca_k8_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p0_mvtec_tile_k8_seed0.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9919120585540149`
- `auroc`: `0.9816017316017316`
- `brier`: `0.2817289050031973`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.3127995220005003`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.005177549954153534`
- `max_f1`: `0.9824561403508771`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.7566479863328344`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_alpha_0p0_mvtec_tile_k8_seed0_head_pca_k8_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
