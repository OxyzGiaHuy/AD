# Run ablation_pca16_mvtec_capsule_k1_seed3_calib_subspace_head_k1_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca16_mvtec_capsule_k1_seed3.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9172222312905136`
- `auroc`: `0.7191862784204228`
- `brier`: `0.16072946811984043`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.16982617417626455`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.001629226699923024`
- `max_f1`: `0.911504424778761`
- `model_storage_mb`: `0.4018745422363281`
- `nll`: `1.8281971001253408`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_pca16_mvtec_capsule_k1_seed3_calib_subspace_head_k1_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
