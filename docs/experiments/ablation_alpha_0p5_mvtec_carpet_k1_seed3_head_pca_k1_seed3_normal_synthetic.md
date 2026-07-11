# Run ablation_alpha_0p5_mvtec_carpet_k1_seed3_head_pca_k1_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p5_mvtec_carpet_k1_seed3.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9823643523484745`
- `auroc`: `0.9345906902086677`
- `brier`: `0.19305169767215988`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.3274015743508298`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.002144835698298919`
- `max_f1`: `0.9294117647058824`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.5768851653326575`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_alpha_0p5_mvtec_carpet_k1_seed3_head_pca_k1_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
