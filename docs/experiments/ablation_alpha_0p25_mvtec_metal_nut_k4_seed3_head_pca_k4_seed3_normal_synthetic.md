# Run ablation_alpha_0p25_mvtec_metal_nut_k4_seed3_head_pca_k4_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p25_mvtec_metal_nut_k4_seed3.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9933573792790855`
- `auroc`: `0.9706744868035191`
- `brier`: `0.20578715320411856`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.3390038360720096`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0034814678942379743`
- `max_f1`: `0.9533678756476683`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6041043018191692`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_alpha_0p25_mvtec_metal_nut_k4_seed3_head_pca_k4_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
