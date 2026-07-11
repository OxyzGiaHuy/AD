# Run ablation_calib_upper_mvtec_toothbrush_k8_seed3_calib_subspace_head_k8_seed3_normal_plus_anomaly_val

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_calib_upper_mvtec_toothbrush_k8_seed3.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9829509612595847`
- `auroc`: `0.9629629629629629`
- `brier`: `0.07470731727383441`
- `calibration_anomaly_val_count`: `3`
- `ece`: `0.11650279059241976`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0015658496473080073`
- `max_f1`: `0.9642857142857143`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `0.21979024547904535`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_calib_upper_mvtec_toothbrush_k8_seed3_calib_subspace_head_k8_seed3_normal_plus_anomaly_val/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
