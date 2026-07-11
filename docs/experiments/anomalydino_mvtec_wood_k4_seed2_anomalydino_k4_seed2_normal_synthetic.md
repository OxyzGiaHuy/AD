# Run anomalydino_mvtec_wood_k4_seed2_anomalydino_k4_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/anomalydino_mvtec_wood_k4_seed2.yaml`
- Dataset: `mvtec`
- Model: `anomalydino`

## Metrics

- `ap`: `0.9872836382792052`
- `auroc`: `0.9605263157894737`
- `brier`: `0.7591961542404946`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.7590008034055672`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.012397691843253148`
- `max_f1`: `0.9508196721311475`
- `model_storage_mb`: `6.0`
- `nll`: `6.702174858139517`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/anomalydino_mvtec_wood_k4_seed2_anomalydino_k4_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
