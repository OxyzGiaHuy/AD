# Run anomalydino_mvtec_hazelnut_k8_seed0_anomalydino_k8_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/anomalydino_mvtec_hazelnut_k8_seed0.yaml`
- Dataset: `mvtec`
- Model: `anomalydino`

## Metrics

- `ap`: `0.9812170107438459`
- `auroc`: `0.965`
- `brier`: `0.6226054146103158`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.621470464804125`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.012422082996503873`
- `max_f1`: `0.927536231884058`
- `model_storage_mb`: `6.0`
- `nll`: `2.906646691854112`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/anomalydino_mvtec_hazelnut_k8_seed0_anomalydino_k8_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
