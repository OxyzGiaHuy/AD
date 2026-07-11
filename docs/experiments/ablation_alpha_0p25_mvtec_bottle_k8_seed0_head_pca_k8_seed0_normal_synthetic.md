# Run ablation_alpha_0p25_mvtec_bottle_k8_seed0_head_pca_k8_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p25_mvtec_bottle_k8_seed0.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9973260236514047`
- `auroc`: `0.9920634920634921`
- `brier`: `0.20658770728053322`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.40635158678135236`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.005061720127621329`
- `max_f1`: `0.9921259842519685`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6058781741042683`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_alpha_0p25_mvtec_bottle_k8_seed0_head_pca_k8_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
