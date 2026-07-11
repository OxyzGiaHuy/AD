# Run ablation_pca128_mvtec_zipper_k1_seed2_calib_subspace_head_k1_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca128_mvtec_zipper_k1_seed2.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9754816126156123`
- `auroc`: `0.915703781512605`
- `brier`: `0.19846138202547892`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.2044075601148289`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0030841837630958746`
- `max_f1`: `0.937007874015748`
- `model_storage_mb`: `0.5659370422363281`
- `nll`: `1.106012751026139`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_pca128_mvtec_zipper_k1_seed2_calib_subspace_head_k1_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
