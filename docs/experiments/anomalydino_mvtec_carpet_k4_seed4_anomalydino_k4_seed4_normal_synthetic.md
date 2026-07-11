# Run anomalydino_mvtec_carpet_k4_seed4_anomalydino_k4_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/anomalydino_mvtec_carpet_k4_seed4.yaml`
- Dataset: `mvtec`
- Model: `anomalydino`

## Metrics

- `ap`: `0.998363852040943`
- `auroc`: `0.9947833065810594`
- `brier`: `0.7575709648482432`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.7558307802286217`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.01252806764573623`
- `max_f1`: `0.9832402234636871`
- `model_storage_mb`: `6.0`
- `nll`: `4.883537704665865`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/anomalydino_mvtec_carpet_k4_seed4_anomalydino_k4_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
