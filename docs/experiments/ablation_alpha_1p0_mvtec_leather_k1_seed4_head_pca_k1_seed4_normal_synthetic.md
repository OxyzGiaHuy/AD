# Run ablation_alpha_1p0_mvtec_leather_k1_seed4_head_pca_k1_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_1p0_mvtec_leather_k1_seed4.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9811675139409539`
- `auroc`: `0.9395380434782609`
- `brier`: `0.18883441542560112`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.03040774358857054`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0034040239369196278`
- `max_f1`: `0.9171270718232044`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.5647213619115834`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_alpha_1p0_mvtec_leather_k1_seed4_head_pca_k1_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
