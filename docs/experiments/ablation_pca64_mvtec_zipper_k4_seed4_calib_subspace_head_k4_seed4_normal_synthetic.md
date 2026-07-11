# Run ablation_pca64_mvtec_zipper_k4_seed4_calib_subspace_head_k4_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca64_mvtec_zipper_k4_seed4.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9945286380517392`
- `auroc`: `0.9813550420168067`
- `brier`: `0.04469497040432857`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.07754127390139941`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0018394349130573652`
- `max_f1`: `0.979253112033195`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `0.1760438638781118`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_pca64_mvtec_zipper_k4_seed4_calib_subspace_head_k4_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
