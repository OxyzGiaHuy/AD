# Run ablation_alpha_0p0_mvtec_toothbrush_k8_seed2_head_pca_k8_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p0_mvtec_toothbrush_k8_seed2.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9875820525723196`
- `auroc`: `0.9694444444444444`
- `brier`: `0.2387444387799766`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.373705472264971`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.004375404190449487`
- `max_f1`: `0.967741935483871`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6706033687831033`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_alpha_0p0_mvtec_toothbrush_k8_seed2_head_pca_k8_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
