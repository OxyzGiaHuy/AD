# Run anomalydino_mvtec_zipper_k4_seed1_anomalydino_k4_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/anomalydino_mvtec_zipper_k4_seed1.yaml`
- Dataset: `mvtec`
- Model: `anomalydino`

## Metrics

- `ap`: `0.9918418672041193`
- `auroc`: `0.9719012605042017`
- `brier`: `0.757556365541285`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.7636611693421539`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.012633249138956828`
- `max_f1`: `0.9666666666666667`
- `model_storage_mb`: `6.0`
- `nll`: `3.1552997876389104`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/anomalydino_mvtec_zipper_k4_seed1_anomalydino_k4_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
