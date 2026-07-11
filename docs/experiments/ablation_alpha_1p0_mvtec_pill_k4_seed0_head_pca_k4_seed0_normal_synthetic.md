# Run ablation_alpha_1p0_mvtec_pill_k4_seed0_head_pca_k4_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_1p0_mvtec_pill_k4_seed0.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.976255007209985`
- `auroc`: `0.911620294599018`
- `brier`: `0.13624973358316317`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.16316077273762872`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0020741464202097075`
- `max_f1`: `0.9436619718309859`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.4484832365077713`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_alpha_1p0_mvtec_pill_k4_seed0_head_pca_k4_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
