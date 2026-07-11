# Run ablation_pca64_mvtec_zipper_k4_seed1_calib_subspace_head_k4_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca64_mvtec_zipper_k4_seed1.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9867537773565089`
- `auroc`: `0.9524684873949579`
- `brier`: `0.12322578407634788`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.14031910209219586`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0025801409331970655`
- `max_f1`: `0.9473684210526315`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `0.5544630280341032`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_pca64_mvtec_zipper_k4_seed1_calib_subspace_head_k4_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
