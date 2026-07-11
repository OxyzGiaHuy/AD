# Run anomalydino_mvtec_wood_k4_seed1_anomalydino_k4_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/anomalydino_mvtec_wood_k4_seed1.yaml`
- Dataset: `mvtec`
- Model: `anomalydino`

## Metrics

- `ap`: `0.983122956425783`
- `auroc`: `0.9517543859649122`
- `brier`: `0.7332724207819479`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.7379813374409193`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.012799835822816137`
- `max_f1`: `0.959349593495935`
- `model_storage_mb`: `6.0`
- `nll`: `3.0984587122955465`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/anomalydino_mvtec_wood_k4_seed1_anomalydino_k4_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
