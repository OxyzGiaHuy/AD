# Run ablation_alpha_0p25_mvtec_carpet_k1_seed0_head_pca_k1_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p25_mvtec_carpet_k1_seed0.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9928320143922632`
- `auroc`: `0.9771268057784912`
- `brier`: `0.20762196784691445`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.39033506823401165`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0019729648454067036`
- `max_f1`: `0.9617486338797814`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6078122213493129`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_alpha_0p25_mvtec_carpet_k1_seed0_head_pca_k1_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
