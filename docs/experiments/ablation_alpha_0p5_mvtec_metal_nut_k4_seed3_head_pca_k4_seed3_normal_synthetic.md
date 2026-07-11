# Run ablation_alpha_0p5_mvtec_metal_nut_k4_seed3_head_pca_k4_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p5_mvtec_metal_nut_k4_seed3.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9914300180752904`
- `auroc`: `0.9613880742913001`
- `brier`: `0.17659507965079263`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.22830561710440597`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0033867726183455923`
- `max_f1`: `0.9508196721311475`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.5423340470314941`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_alpha_0p5_mvtec_metal_nut_k4_seed3_head_pca_k4_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
