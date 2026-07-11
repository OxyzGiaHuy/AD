# Run ablation_pca16_mvtec_transistor_k8_seed3_calib_subspace_head_k8_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca16_mvtec_transistor_k8_seed3.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.7173306801069731`
- `auroc`: `0.7970833333333334`
- `brier`: `0.20623103490620154`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.20668732319725674`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.004831134714186192`
- `max_f1`: `0.7157894736842105`
- `model_storage_mb`: `0.4018745422363281`
- `nll`: `0.6966410838128985`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_pca16_mvtec_transistor_k8_seed3_calib_subspace_head_k8_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
