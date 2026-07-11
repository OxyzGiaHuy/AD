# Run anomalydino_mvtec_hazelnut_k4_seed0_anomalydino_k4_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/anomalydino_mvtec_hazelnut_k4_seed0.yaml`
- Dataset: `mvtec`
- Model: `anomalydino`

## Metrics

- `ap`: `0.9865716379204676`
- `auroc`: `0.9753571428571428`
- `brier`: `0.6357016093779686`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.6353658067950164`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.012319918840446255`
- `max_f1`: `0.9583333333333334`
- `model_storage_mb`: `6.0`
- `nll`: `4.932882076459436`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/anomalydino_mvtec_hazelnut_k4_seed0_anomalydino_k4_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
