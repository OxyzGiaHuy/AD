# Run ablation_pca16_mvtec_metal_nut_k8_seed1_calib_subspace_head_k8_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca16_mvtec_metal_nut_k8_seed1.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9243047277958482`
- `auroc`: `0.7839687194525904`
- `brier`: `0.11333556886398974`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.11462256973204404`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0017700460779926052`
- `max_f1`: `0.9292929292929293`
- `model_storage_mb`: `0.4018745422363281`
- `nll`: `0.41461515063128024`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_pca16_mvtec_metal_nut_k8_seed1_calib_subspace_head_k8_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
