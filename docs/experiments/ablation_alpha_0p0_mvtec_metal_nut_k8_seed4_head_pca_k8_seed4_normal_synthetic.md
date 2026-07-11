# Run ablation_alpha_0p0_mvtec_metal_nut_k8_seed4_head_pca_k8_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p0_mvtec_metal_nut_k8_seed4.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9818534890482227`
- `auroc`: `0.9354838709677419`
- `brier`: `0.2554280304951747`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.3868795970211859`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.004546535436225974`
- `max_f1`: `0.9528795811518325`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.7039619594108619`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_alpha_0p0_mvtec_metal_nut_k8_seed4_head_pca_k8_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
