# Run ablation_pca16_mvtec_hazelnut_k1_seed0_calib_subspace_head_k1_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca16_mvtec_hazelnut_k1_seed0.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9288283811786414`
- `auroc`: `0.8839285714285714`
- `brier`: `0.3308262542963439`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.3158329638567838`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0017638393085111271`
- `max_f1`: `0.868421052631579`
- `model_storage_mb`: `0.4018745422363281`
- `nll`: `1.1343232877866283`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_pca16_mvtec_hazelnut_k1_seed0_calib_subspace_head_k1_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
