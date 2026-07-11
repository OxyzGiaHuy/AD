# Run ablation_pca16_mvtec_transistor_k1_seed0_calib_subspace_head_k1_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca16_mvtec_transistor_k1_seed0.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.6785785108222189`
- `auroc`: `0.7395833333333334`
- `brier`: `0.2886315618446428`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.2848838938854896`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0017324748449027538`
- `max_f1`: `0.6363636363636364`
- `model_storage_mb`: `0.4018745422363281`
- `nll`: `1.3040923850509447`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_pca16_mvtec_transistor_k1_seed0_calib_subspace_head_k1_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
