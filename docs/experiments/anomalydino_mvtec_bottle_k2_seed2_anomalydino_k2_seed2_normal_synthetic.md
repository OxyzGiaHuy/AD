# Run anomalydino_mvtec_bottle_k2_seed2_anomalydino_k2_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/anomalydino_mvtec_bottle_k2_seed2.yaml`
- Dataset: `mvtec`
- Model: `anomalydino`

## Metrics

- `ap`: `0.9984993380055517`
- `auroc`: `0.9952380952380953`
- `brier`: `0.24096385542168675`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.24096385542168675`
- `k_shot`: `2`
- `latency_sec_per_image`: `0.00905619723251067`
- `max_f1`: `0.984375`
- `model_storage_mb`: `4.0107421875`
- `nll`: `4.438718257934363`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `2738`

## Notes

- Predictions written to outputs/anomalydino_mvtec_bottle_k2_seed2_anomalydino_k2_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
