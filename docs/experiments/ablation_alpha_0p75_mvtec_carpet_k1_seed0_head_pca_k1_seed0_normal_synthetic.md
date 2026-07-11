# Run ablation_alpha_0p75_mvtec_carpet_k1_seed0_head_pca_k1_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p75_mvtec_carpet_k1_seed0.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9864849685266678`
- `auroc`: `0.9554574638844302`
- `brier`: `0.17834637423499536`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.31739633664106703`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0028858112855854197`
- `max_f1`: `0.9502762430939227`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.543682493522075`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_alpha_0p75_mvtec_carpet_k1_seed0_head_pca_k1_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
