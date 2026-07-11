# Run ablation_pca32_mvtec_cable_k1_seed0_calib_subspace_head_k1_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca32_mvtec_cable_k1_seed0.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9397125122595752`
- `auroc`: `0.8856821589205397`
- `brier`: `0.38658994625896254`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.38661753694216416`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.001598319374024868`
- `max_f1`: `0.8654970760233918`
- `model_storage_mb`: `0.4253120422363281`
- `nll`: `5.4090649507753685`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_pca32_mvtec_cable_k1_seed0_calib_subspace_head_k1_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
