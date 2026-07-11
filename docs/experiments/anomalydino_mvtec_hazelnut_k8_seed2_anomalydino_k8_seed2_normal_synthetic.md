# Run anomalydino_mvtec_hazelnut_k8_seed2_anomalydino_k8_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/anomalydino_mvtec_hazelnut_k8_seed2.yaml`
- Dataset: `mvtec`
- Model: `anomalydino`

## Metrics

- `ap`: `0.9986065942240586`
- `auroc`: `0.9975`
- `brier`: `0.6236807213903585`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.6221355925568125`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.012768242474306713`
- `max_f1`: `0.9857142857142858`
- `model_storage_mb`: `6.0`
- `nll`: `2.9565289579450225`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/anomalydino_mvtec_hazelnut_k8_seed2_anomalydino_k8_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
