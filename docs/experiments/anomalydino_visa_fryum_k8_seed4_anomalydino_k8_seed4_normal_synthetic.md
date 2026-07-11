# Run anomalydino_visa_fryum_k8_seed4_anomalydino_k8_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/visa_full/anomalydino_visa_fryum_k8_seed4.yaml`
- Dataset: `visa`
- Model: `anomalydino`

## Metrics

- `ap`: `0.9739972309498333`
- `auroc`: `0.9458`
- `brier`: `0.5255365113664819`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.5494001332918803`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.08363216883192459`
- `max_f1`: `0.919431279620853`
- `model_storage_mb`: `6.0`
- `nll`: `1.4776385057071824`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/anomalydino_visa_fryum_k8_seed4_anomalydino_k8_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
