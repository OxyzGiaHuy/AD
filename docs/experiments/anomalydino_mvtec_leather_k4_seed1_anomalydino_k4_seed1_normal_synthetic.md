# Run anomalydino_mvtec_leather_k4_seed1_anomalydino_k4_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/anomalydino_mvtec_leather_k4_seed1.yaml`
- Dataset: `mvtec`
- Model: `anomalydino`

## Metrics

- `ap`: `0.9936712144143982`
- `auroc`: `0.9833559782608695`
- `brier`: `0.25806383067861355`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.2580641734023248`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.012661582009205896`
- `max_f1`: `0.9680851063829787`
- `model_storage_mb`: `6.0`
- `nll`: `4.211280058862752`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/anomalydino_mvtec_leather_k4_seed1_anomalydino_k4_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
