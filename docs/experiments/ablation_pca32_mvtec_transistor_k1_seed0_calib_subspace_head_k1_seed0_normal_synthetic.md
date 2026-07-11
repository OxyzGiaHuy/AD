# Run ablation_pca32_mvtec_transistor_k1_seed0_calib_subspace_head_k1_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca32_mvtec_transistor_k1_seed0.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.7442692521892733`
- `auroc`: `0.79`
- `brier`: `0.4833719107488861`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.5042918174667284`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0018960589542984963`
- `max_f1`: `0.6842105263157895`
- `model_storage_mb`: `0.4253120422363281`
- `nll`: `5.73364340617471`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_pca32_mvtec_transistor_k1_seed0_calib_subspace_head_k1_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
