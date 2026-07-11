# Run ablation_alpha_0p0_mvtec_carpet_k1_seed0_head_pca_k1_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p0_mvtec_carpet_k1_seed0.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9964061228892744`
- `auroc`: `0.9887640449438202`
- `brier`: `0.2330737046287898`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.35164330326593835`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0017850541660928319`
- `max_f1`: `0.9834254143646409`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6592582321730494`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_alpha_0p0_mvtec_carpet_k1_seed0_head_pca_k1_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
