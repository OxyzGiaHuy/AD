# Run ablation_alpha_0p25_mvtec_metal_nut_k8_seed2_head_pca_k8_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p25_mvtec_metal_nut_k8_seed2.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9947562682554815`
- `auroc`: `0.9775171065493646`
- `brier`: `0.2062436789925248`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.3871440801931465`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0039114487721868185`
- `max_f1`: `0.9680851063829787`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6051112340352324`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_alpha_0p25_mvtec_metal_nut_k8_seed2_head_pca_k8_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
