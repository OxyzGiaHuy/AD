# Run anomalydino_mvtec_wood_k1_seed3_anomalydino_k1_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/anomalydino_mvtec_wood_k1_seed3.yaml`
- Dataset: `mvtec`
- Model: `anomalydino`

## Metrics

- `ap`: `0.9895900331160316`
- `auroc`: `0.9692982456140351`
- `brier`: `0.24050632911392406`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.240506329113924`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.005041773041969613`
- `max_f1`: `0.9672131147540983`
- `model_storage_mb`: `2.00537109375`
- `nll`: `4.430290311893983`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/anomalydino_mvtec_wood_k1_seed3_anomalydino_k1_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
