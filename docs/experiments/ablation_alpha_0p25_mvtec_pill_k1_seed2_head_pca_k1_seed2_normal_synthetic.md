# Run ablation_alpha_0p25_mvtec_pill_k1_seed2_head_pca_k1_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p25_mvtec_pill_k1_seed2.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9846506276279489`
- `auroc`: `0.9236224768139661`
- `brier`: `0.20701476617834955`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.3026045293151261`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0020178327571132226`
- `max_f1`: `0.9473684210526315`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6066580165283403`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_alpha_0p25_mvtec_pill_k1_seed2_head_pca_k1_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
