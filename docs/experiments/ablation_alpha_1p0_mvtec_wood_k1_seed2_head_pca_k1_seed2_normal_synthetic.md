# Run ablation_alpha_1p0_mvtec_wood_k1_seed2_head_pca_k1_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_1p0_mvtec_wood_k1_seed2.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9806354261584934`
- `auroc`: `0.9342105263157895`
- `brier`: `0.18419181314819175`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.041630887532536076`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0017784362116569205`
- `max_f1`: `0.9243697478991597`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.5555804786312345`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_alpha_1p0_mvtec_wood_k1_seed2_head_pca_k1_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
