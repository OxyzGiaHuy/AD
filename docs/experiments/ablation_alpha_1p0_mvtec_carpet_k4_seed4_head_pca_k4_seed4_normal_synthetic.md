# Run ablation_alpha_1p0_mvtec_carpet_k4_seed4_head_pca_k4_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_1p0_mvtec_carpet_k4_seed4.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.979157478687066`
- `auroc`: `0.92776886035313`
- `brier`: `0.14799995185160092`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.2400594720473656`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.00214728262498338`
- `max_f1`: `0.9204545454545454`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.46854460040143203`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_alpha_1p0_mvtec_carpet_k4_seed4_head_pca_k4_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
