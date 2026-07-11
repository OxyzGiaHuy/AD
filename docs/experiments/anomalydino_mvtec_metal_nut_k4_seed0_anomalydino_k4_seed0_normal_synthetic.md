# Run anomalydino_mvtec_metal_nut_k4_seed0_anomalydino_k4_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/anomalydino_mvtec_metal_nut_k4_seed0.yaml`
- Dataset: `mvtec`
- Model: `anomalydino`

## Metrics

- `ap`: `0.9941334954563327`
- `auroc`: `0.9755620723362659`
- `brier`: `0.7868740206057627`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.7923249021091539`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.01255577384777691`
- `max_f1`: `0.9637305699481865`
- `model_storage_mb`: `6.0`
- `nll`: `3.512748733588852`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/anomalydino_mvtec_metal_nut_k4_seed0_anomalydino_k4_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
