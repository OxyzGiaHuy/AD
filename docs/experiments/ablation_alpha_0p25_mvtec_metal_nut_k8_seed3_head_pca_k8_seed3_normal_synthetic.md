# Run ablation_alpha_0p25_mvtec_metal_nut_k8_seed3_head_pca_k8_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p25_mvtec_metal_nut_k8_seed3.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9987433405694975`
- `auroc`: `0.9946236559139785`
- `brier`: `0.20531453444415876`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.41398790737856994`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0018188391366730566`
- `max_f1`: `0.983957219251337`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6032433736595653`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_alpha_0p25_mvtec_metal_nut_k8_seed3_head_pca_k8_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
