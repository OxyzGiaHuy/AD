# Run ablation_pca128_mvtec_capsule_k8_seed3_calib_subspace_head_k8_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca128_mvtec_capsule_k8_seed3.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9512627206655365`
- `auroc`: `0.8284802552852014`
- `brier`: `0.10977918907518461`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.11898476881359592`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.001716527043644226`
- `max_f1`: `0.9417040358744395`
- `model_storage_mb`: `0.5659370422363281`
- `nll`: `0.6603472383292026`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_pca128_mvtec_capsule_k8_seed3_calib_subspace_head_k8_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
