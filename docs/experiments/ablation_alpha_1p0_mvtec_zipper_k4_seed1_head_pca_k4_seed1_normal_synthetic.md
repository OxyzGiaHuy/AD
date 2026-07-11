# Run ablation_alpha_1p0_mvtec_zipper_k4_seed1_head_pca_k4_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_1p0_mvtec_zipper_k4_seed1.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9895313702014811`
- `auroc`: `0.9655987394957983`
- `brier`: `0.154494063424715`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.17678667930577768`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.011851735894155028`
- `max_f1`: `0.9711934156378601`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.4865416021454768`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_alpha_1p0_mvtec_zipper_k4_seed1_head_pca_k4_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
