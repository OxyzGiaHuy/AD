# Run ablation_alpha_0p25_mvtec_transistor_k4_seed1_head_pca_k4_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p25_mvtec_transistor_k4_seed1.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.7920962939132398`
- `auroc`: `0.8466666666666667`
- `brier`: `0.25344164031276534`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.1472104728221893`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0031155775859951973`
- `max_f1`: `0.7415730337078652`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6999614764366809`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_alpha_0p25_mvtec_transistor_k4_seed1_head_pca_k4_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
