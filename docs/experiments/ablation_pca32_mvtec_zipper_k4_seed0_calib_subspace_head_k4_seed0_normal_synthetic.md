# Run ablation_pca32_mvtec_zipper_k4_seed0_calib_subspace_head_k4_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca32_mvtec_zipper_k4_seed0.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9836750855805096`
- `auroc`: `0.9424894957983193`
- `brier`: `0.12797824540326588`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.1287362335730862`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0020154636747987064`
- `max_f1`: `0.9516129032258065`
- `model_storage_mb`: `0.4253120422363281`
- `nll`: `0.40217317975494243`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_pca32_mvtec_zipper_k4_seed0_calib_subspace_head_k4_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
