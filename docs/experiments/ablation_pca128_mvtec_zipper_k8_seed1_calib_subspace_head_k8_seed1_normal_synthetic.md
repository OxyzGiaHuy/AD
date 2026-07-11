# Run ablation_pca128_mvtec_zipper_k8_seed1_calib_subspace_head_k8_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca128_mvtec_zipper_k8_seed1.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9838785420443794`
- `auroc`: `0.9427521008403361`
- `brier`: `0.08818001342316639`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.09970066185565724`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.001651216076304581`
- `max_f1`: `0.9551020408163265`
- `model_storage_mb`: `0.5659370422363281`
- `nll`: `0.3957113720993422`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_pca128_mvtec_zipper_k8_seed1_calib_subspace_head_k8_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
