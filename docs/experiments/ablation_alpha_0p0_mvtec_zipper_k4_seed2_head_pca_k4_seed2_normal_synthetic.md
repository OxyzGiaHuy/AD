# Run ablation_alpha_0p0_mvtec_zipper_k4_seed2_head_pca_k4_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p0_mvtec_zipper_k4_seed2.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9796410748389817`
- `auroc`: `0.9272584033613446`
- `brier`: `0.24714688565061974`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.3074931117477796`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0030823341934688832`
- `max_f1`: `0.9402390438247012`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6873646410769788`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_alpha_0p0_mvtec_zipper_k4_seed2_head_pca_k4_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
