# Run ablation_alpha_0p5_mvtec_screw_k4_seed0_head_pca_k4_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p5_mvtec_screw_k4_seed0.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.8628603210558099`
- `auroc`: `0.7204345152695224`
- `brier`: `0.19973933430296514`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.1440016966313123`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0016975569305941463`
- `max_f1`: `0.8803088803088803`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.5904469896182769`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_alpha_0p5_mvtec_screw_k4_seed0_head_pca_k4_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
