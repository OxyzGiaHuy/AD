# Run ablation_calib_upper_mvtec_capsule_k8_seed3_calib_subspace_head_k8_seed3_normal_plus_anomaly_val

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_calib_upper_mvtec_capsule_k8_seed3.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9368912370956549`
- `auroc`: `0.7988581466842336`
- `brier`: `0.12723350005191814`
- `calibration_anomaly_val_count`: `10`
- `ece`: `0.11958718574682223`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0014477337970108283`
- `max_f1`: `0.9326923076923077`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `0.47671982875087376`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_calib_upper_mvtec_capsule_k8_seed3_calib_subspace_head_k8_seed3_normal_plus_anomaly_val/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
