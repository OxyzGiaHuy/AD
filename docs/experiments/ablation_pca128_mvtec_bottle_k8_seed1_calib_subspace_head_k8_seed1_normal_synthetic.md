# Run ablation_pca128_mvtec_bottle_k8_seed1_calib_subspace_head_k8_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca128_mvtec_bottle_k8_seed1.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9961161021368834`
- `auroc`: `0.9888888888888889`
- `brier`: `0.10173941172511891`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.13280606058886252`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.00416257160614772`
- `max_f1`: `0.9921259842519685`
- `model_storage_mb`: `0.5659370422363281`
- `nll`: `0.4241915371011403`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_pca128_mvtec_bottle_k8_seed1_calib_subspace_head_k8_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
