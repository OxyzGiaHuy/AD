# Run ablation_alpha_1p0_mvtec_metal_nut_k4_seed3_head_pca_k4_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_1p0_mvtec_metal_nut_k4_seed3.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9826795823662828`
- `auroc`: `0.9296187683284457`
- `brier`: `0.1525699275644717`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.1077565498974013`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.002271163447395615`
- `max_f1`: `0.9424083769633508`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.4832257418461443`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_alpha_1p0_mvtec_metal_nut_k4_seed3_head_pca_k4_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
