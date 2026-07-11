# Run anomalydino_mvtec_hazelnut_k8_seed1_anomalydino_k8_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/anomalydino_mvtec_hazelnut_k8_seed1.yaml`
- Dataset: `mvtec`
- Model: `anomalydino`

## Metrics

- `ap`: `0.997058143474486`
- `auroc`: `0.9946428571428572`
- `brier`: `0.618695968202034`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.6170499562751501`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.012794777649370107`
- `max_f1`: `0.971830985915493`
- `model_storage_mb`: `6.0`
- `nll`: `2.740092147901058`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/anomalydino_mvtec_hazelnut_k8_seed1_anomalydino_k8_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
