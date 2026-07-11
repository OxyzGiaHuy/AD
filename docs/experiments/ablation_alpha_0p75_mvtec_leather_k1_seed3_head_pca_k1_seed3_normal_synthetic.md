# Run ablation_alpha_0p75_mvtec_leather_k1_seed3_head_pca_k1_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p75_mvtec_leather_k1_seed3.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9971609983860583`
- `auroc`: `0.990828804347826`
- `brier`: `0.1860630860466447`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.38056798567695005`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.00300168136375085`
- `max_f1`: `0.978021978021978`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.5597902674410496`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_alpha_0p75_mvtec_leather_k1_seed3_head_pca_k1_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
