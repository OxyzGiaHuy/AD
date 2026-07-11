# Run ablation_alpha_0p25_mvtec_metal_nut_k1_seed1_head_pca_k1_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p25_mvtec_metal_nut_k1_seed1.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9874932470865069`
- `auroc`: `0.9452590420332356`
- `brier`: `0.21552102653255187`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.32365549232648766`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.002530858568523241`
- `max_f1`: `0.9424083769633508`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6238710101990705`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_alpha_0p25_mvtec_metal_nut_k1_seed1_head_pca_k1_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
