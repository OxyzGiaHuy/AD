# Run ablation_alpha_0p0_mvtec_zipper_k4_seed4_head_pca_k4_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p0_mvtec_zipper_k4_seed4.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9945286380517392`
- `auroc`: `0.9813550420168067`
- `brier`: `0.23490973926327588`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.393293172121048`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0028572936499158277`
- `max_f1`: `0.979253112033195`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6628485241072614`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_alpha_0p0_mvtec_zipper_k4_seed4_head_pca_k4_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
