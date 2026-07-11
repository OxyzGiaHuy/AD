# Run anomalydino_mvtec_tile_k8_seed1_anomalydino_k8_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/anomalydino_mvtec_tile_k8_seed1.yaml`
- Dataset: `mvtec`
- Model: `anomalydino`

## Metrics

- `ap`: `0.9989831346503587`
- `auroc`: `0.9974747474747475`
- `brier`: `0.7167870693018751`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.7150366264684589`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.01239279525465945`
- `max_f1`: `0.9940828402366864`
- `model_storage_mb`: `6.0`
- `nll`: `5.604342742309153`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/anomalydino_mvtec_tile_k8_seed1_anomalydino_k8_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
