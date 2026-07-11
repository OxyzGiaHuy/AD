# Run ablation_alpha_0p75_mvtec_hazelnut_k4_seed3_head_pca_k4_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p75_mvtec_hazelnut_k4_seed3.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9723201485360864`
- `auroc`: `0.9435714285714286`
- `brier`: `0.23068182892990136`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.05257987705144009`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.005969176492230458`
- `max_f1`: `0.9333333333333333`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6536402082650196`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_alpha_0p75_mvtec_hazelnut_k4_seed3_head_pca_k4_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
