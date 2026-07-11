# Run ablation_pca64_mvtec_metal_nut_k8_seed1_calib_subspace_head_k8_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca64_mvtec_metal_nut_k8_seed1.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.992689452080543`
- `auroc`: `0.9711632453567938`
- `brier`: `0.0973841871275389`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.11416597022958426`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0030254840202953506`
- `max_f1`: `0.9633507853403142`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `0.5943212592712784`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_pca64_mvtec_metal_nut_k8_seed1_calib_subspace_head_k8_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
