# Run ablation_pca128_mvtec_metal_nut_k8_seed0_calib_subspace_head_k8_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca128_mvtec_metal_nut_k8_seed0.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9968667771886552`
- `auroc`: `0.9868035190615836`
- `brier`: `0.08125453623834486`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.09290776707677414`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0022560049010359722`
- `max_f1`: `0.978494623655914`
- `model_storage_mb`: `0.5659370422363281`
- `nll`: `0.3374641311567561`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_pca128_mvtec_metal_nut_k8_seed0_calib_subspace_head_k8_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
