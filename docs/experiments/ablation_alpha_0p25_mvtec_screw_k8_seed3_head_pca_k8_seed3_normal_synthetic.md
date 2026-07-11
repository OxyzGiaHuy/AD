# Run ablation_alpha_0p25_mvtec_screw_k8_seed3_head_pca_k8_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p25_mvtec_screw_k8_seed3.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9004735236243914`
- `auroc`: `0.8026234884197582`
- `brier`: `0.21778770517895688`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.2645201113075018`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0018695927341468633`
- `max_f1`: `0.8923076923076924`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.628308877541221`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_alpha_0p25_mvtec_screw_k8_seed3_head_pca_k8_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
