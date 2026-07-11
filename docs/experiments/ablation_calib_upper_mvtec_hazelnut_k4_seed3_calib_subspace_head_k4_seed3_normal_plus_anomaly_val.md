# Run ablation_calib_upper_mvtec_hazelnut_k4_seed3_calib_subspace_head_k4_seed3_normal_plus_anomaly_val

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_calib_upper_mvtec_hazelnut_k4_seed3.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9881452611361367`
- `auroc`: `0.9833333333333333`
- `brier`: `0.09158031351006206`
- `calibration_anomaly_val_count`: `7`
- `ece`: `0.1568227994789198`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0018599121424468976`
- `max_f1`: `0.9606299212598425`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `0.29920689769366493`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_calib_upper_mvtec_hazelnut_k4_seed3_calib_subspace_head_k4_seed3_normal_plus_anomaly_val/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
