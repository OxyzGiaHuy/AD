# Run ablation_pca128_mvtec_zipper_k8_seed2_calib_subspace_head_k8_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca128_mvtec_zipper_k8_seed2.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.984007112562452`
- `auroc`: `0.944327731092437`
- `brier`: `0.09472555754949398`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.11188929723205658`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.002398657174595934`
- `max_f1`: `0.9512195121951219`
- `model_storage_mb`: `0.5659370422363281`
- `nll`: `0.4583497703602077`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_pca128_mvtec_zipper_k8_seed2_calib_subspace_head_k8_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
