# Run anomalydino_visa_pipe_fryum_k8_seed1_anomalydino_k8_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/visa_full/anomalydino_visa_pipe_fryum_k8_seed1.yaml`
- Dataset: `visa`
- Model: `anomalydino`

## Metrics

- `ap`: `0.9907580149343326`
- `auroc`: `0.9808`
- `brier`: `0.6507514839698587`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.6497298828419298`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.11169612474739551`
- `max_f1`: `0.9595959595959596`
- `model_storage_mb`: `6.0`
- `nll`: `2.975674523194519`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/anomalydino_visa_pipe_fryum_k8_seed1_anomalydino_k8_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
