# Run ablation_pca64_mvtec_zipper_k4_seed0_calib_subspace_head_k4_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca64_mvtec_zipper_k4_seed0.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9862252259134936`
- `auroc`: `0.9506302521008403`
- `brier`: `0.10846991075975258`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.12494799790792903`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0032021441059002023`
- `max_f1`: `0.9512195121951219`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `0.36684418946591046`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_pca64_mvtec_zipper_k4_seed0_calib_subspace_head_k4_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
