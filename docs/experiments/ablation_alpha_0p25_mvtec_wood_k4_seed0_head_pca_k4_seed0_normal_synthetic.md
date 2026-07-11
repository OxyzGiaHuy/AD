# Run ablation_alpha_0p25_mvtec_wood_k4_seed0_head_pca_k4_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p25_mvtec_wood_k4_seed0.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9954007059779173`
- `auroc`: `0.9850877192982456`
- `brier`: `0.21572988372471388`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.3812397137472901`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.002963720644010773`
- `max_f1`: `0.9672131147540983`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6242946537170995`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_alpha_0p25_mvtec_wood_k4_seed0_head_pca_k4_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
