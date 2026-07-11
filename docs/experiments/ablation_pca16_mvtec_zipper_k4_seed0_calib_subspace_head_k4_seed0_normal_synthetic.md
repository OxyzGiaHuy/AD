# Run ablation_pca16_mvtec_zipper_k4_seed0_calib_subspace_head_k4_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca16_mvtec_zipper_k4_seed0.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9757336228984373`
- `auroc`: `0.915703781512605`
- `brier`: `0.0949047185471224`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.08656523131228833`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0020121622041163853`
- `max_f1`: `0.9402390438247012`
- `model_storage_mb`: `0.4018745422363281`
- `nll`: `0.3074153803284016`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_pca16_mvtec_zipper_k4_seed0_calib_subspace_head_k4_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
