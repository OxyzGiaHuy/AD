# Run ablation_alpha_0p25_mvtec_transistor_k1_seed0_head_pca_k1_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p25_mvtec_transistor_k1_seed0.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.8003983284029343`
- `auroc`: `0.8175`
- `brier`: `0.25772292002467523`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.14760253548622126`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.001773405894637108`
- `max_f1`: `0.7160493827160493`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.7085930901700189`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_alpha_0p25_mvtec_transistor_k1_seed0_head_pca_k1_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
