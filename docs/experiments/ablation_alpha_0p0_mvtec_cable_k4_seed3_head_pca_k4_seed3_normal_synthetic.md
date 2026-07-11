# Run ablation_alpha_0p0_mvtec_cable_k4_seed3_head_pca_k4_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p0_mvtec_cable_k4_seed3.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9283605560977565`
- `auroc`: `0.8727511244377811`
- `brier`: `0.243877289587651`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.21651877721150709`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.00408557515591383`
- `max_f1`: `0.845360824742268`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.680884354472921`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_alpha_0p0_mvtec_cable_k4_seed3_head_pca_k4_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
