# Run ablation_pca16_mvtec_cable_k1_seed0_calib_subspace_head_k1_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca16_mvtec_cable_k1_seed0.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.8948150873656028`
- `auroc`: `0.8318965517241379`
- `brier`: `0.330833435109482`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.34281542828500583`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.001971752718091011`
- `max_f1`: `0.8148148148148148`
- `model_storage_mb`: `0.4018745422363281`
- `nll`: `3.3576319777474852`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_pca16_mvtec_cable_k1_seed0_calib_subspace_head_k1_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
