# Run anomalydino_mvtec_screw_k1_seed1_anomalydino_k1_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/anomalydino_mvtec_screw_k1_seed1.yaml`
- Dataset: `mvtec`
- Model: `anomalydino`

## Metrics

- `ap`: `0.8665656738762875`
- `auroc`: `0.6653002664480426`
- `brier`: `0.25625`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.25625`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0047701399424113335`
- `max_f1`: `0.8530465949820788`
- `model_storage_mb`: `2.00537109375`
- `nll`: `4.720299446787697`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/anomalydino_mvtec_screw_k1_seed1_anomalydino_k1_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
