# Run ablation_alpha_0p25_mvtec_transistor_k4_seed0_head_pca_k4_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p25_mvtec_transistor_k4_seed0.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.8023858701285638`
- `auroc`: `0.8316666666666667`
- `brier`: `0.2543370657356154`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.1460886800289154`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.003435984402894974`
- `max_f1`: `0.7155963302752294`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.7017715750689472`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_alpha_0p25_mvtec_transistor_k4_seed0_head_pca_k4_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
