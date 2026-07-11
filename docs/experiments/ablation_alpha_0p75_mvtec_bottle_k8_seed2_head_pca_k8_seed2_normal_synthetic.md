# Run ablation_alpha_0p75_mvtec_bottle_k8_seed2_head_pca_k8_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p75_mvtec_bottle_k8_seed2.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9880655803586406`
- `auroc`: `0.9658730158730159`
- `brier`: `0.16681065760064337`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.23529528207089534`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.004506128963576742`
- `max_f1`: `0.9682539682539683`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.5179087018010142`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_alpha_0p75_mvtec_bottle_k8_seed2_head_pca_k8_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
