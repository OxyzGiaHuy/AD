# Run ablation_pca32_mvtec_leather_k1_seed0_calib_subspace_head_k1_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca32_mvtec_leather_k1_seed0.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9975590327732896`
- `auroc`: `0.9928668478260869`
- `brier`: `0.22586957223481308`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.2379509888349041`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0015442414629843928`
- `max_f1`: `0.9732620320855615`
- `model_storage_mb`: `0.4253120422363281`
- `nll`: `2.545844400312777`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_pca32_mvtec_leather_k1_seed0_calib_subspace_head_k1_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
