# Run anomalydino_mvtec_wood_k1_seed0_anomalydino_k1_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/anomalydino_mvtec_wood_k1_seed0.yaml`
- Dataset: `mvtec`
- Model: `anomalydino`

## Metrics

- `ap`: `0.9770297278241749`
- `auroc`: `0.9350877192982456`
- `brier`: `0.24050632911392406`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.240506329113924`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.004880988663887676`
- `max_f1`: `0.9523809523809523`
- `model_storage_mb`: `2.00537109375`
- `nll`: `4.430290311893983`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/anomalydino_mvtec_wood_k1_seed0_anomalydino_k1_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
