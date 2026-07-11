# Run ablation_alpha_0p25_mvtec_capsule_k1_seed2_head_pca_k1_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p25_mvtec_capsule_k1_seed2.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.942459335760622`
- `auroc`: `0.7921818907060232`
- `brier`: `0.20920180188768947`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.27014101815946173`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0025811284272508187`
- `max_f1`: `0.9159663865546218`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6110293828155535`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_alpha_0p25_mvtec_capsule_k1_seed2_head_pca_k1_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
