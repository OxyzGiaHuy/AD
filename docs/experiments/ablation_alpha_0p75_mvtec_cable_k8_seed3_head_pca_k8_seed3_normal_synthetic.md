# Run ablation_alpha_0p75_mvtec_cable_k8_seed3_head_pca_k8_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p75_mvtec_cable_k8_seed3.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9431846457865213`
- `auroc`: `0.8841829085457271`
- `brier`: `0.23482172055255357`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.06662708878517148`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.003912770909567674`
- `max_f1`: `0.8941176470588236`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6616449493283346`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_alpha_0p75_mvtec_cable_k8_seed3_head_pca_k8_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
