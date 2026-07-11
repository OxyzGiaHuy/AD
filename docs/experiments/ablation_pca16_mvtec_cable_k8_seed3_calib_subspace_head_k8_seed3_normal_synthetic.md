# Run ablation_pca16_mvtec_cable_k8_seed3_calib_subspace_head_k8_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca16_mvtec_cable_k8_seed3.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.8672298554198288`
- `auroc`: `0.7949775112443778`
- `brier`: `0.24463075846854893`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.24123231490453093`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.002294073229034742`
- `max_f1`: `0.8`
- `model_storage_mb`: `0.4018745422363281`
- `nll`: `0.9669570839105783`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_pca16_mvtec_cable_k8_seed3_calib_subspace_head_k8_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
