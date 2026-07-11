# Run ablation_pca128_mvtec_metal_nut_k8_seed3_calib_subspace_head_k8_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca128_mvtec_metal_nut_k8_seed3.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9991007347038525`
- `auroc`: `0.9960899315738025`
- `brier`: `0.039813751941962246`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.057346308255649125`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0023053126652603563`
- `max_f1`: `0.989247311827957`
- `model_storage_mb`: `0.5659370422363281`
- `nll`: `0.1317199737943969`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_pca128_mvtec_metal_nut_k8_seed3_calib_subspace_head_k8_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
