# Run ablation_alpha_0p25_mvtec_cable_k8_seed3_head_pca_k8_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p25_mvtec_cable_k8_seed3.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9361288311155712`
- `auroc`: `0.8770614692653673`
- `brier`: `0.22981750430713457`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.07961427847544358`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.002484556014339129`
- `max_f1`: `0.872093023255814`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6523985792537937`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_alpha_0p25_mvtec_cable_k8_seed3_head_pca_k8_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
