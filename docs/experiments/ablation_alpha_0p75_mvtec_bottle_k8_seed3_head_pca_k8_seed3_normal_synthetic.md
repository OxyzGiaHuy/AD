# Run ablation_alpha_0p75_mvtec_bottle_k8_seed3_head_pca_k8_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p75_mvtec_bottle_k8_seed3.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9896080789681952`
- `auroc`: `0.9714285714285714`
- `brier`: `0.17328835945005208`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.2896704020270382`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0018553370722087033`
- `max_f1`: `0.96875`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.5330565989665487`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_alpha_0p75_mvtec_bottle_k8_seed3_head_pca_k8_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
