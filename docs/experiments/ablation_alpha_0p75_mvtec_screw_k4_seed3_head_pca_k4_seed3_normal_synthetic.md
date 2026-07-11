# Run ablation_alpha_0p75_mvtec_screw_k4_seed3_head_pca_k4_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p75_mvtec_screw_k4_seed3.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.8410058116469452`
- `auroc`: `0.6913301906128305`
- `brier`: `0.19054585738121171`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.12095914930105206`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0019282123306766153`
- `max_f1`: `0.8689138576779026`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.5695033122066862`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_alpha_0p75_mvtec_screw_k4_seed3_head_pca_k4_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
