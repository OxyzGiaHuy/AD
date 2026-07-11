# Run ablation_calib_upper_mvtec_carpet_k8_seed3_calib_subspace_head_k8_seed3_normal_plus_anomaly_val

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_calib_upper_mvtec_carpet_k8_seed3.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9967990840780031`
- `auroc`: `0.9907407407407407`
- `brier`: `0.030223799010672736`
- `calibration_anomaly_val_count`: `8`
- `ece`: `0.047856661627803894`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0015236597781607864`
- `max_f1`: `0.9759036144578314`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `0.10552536387029098`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_calib_upper_mvtec_carpet_k8_seed3_calib_subspace_head_k8_seed3_normal_plus_anomaly_val/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
