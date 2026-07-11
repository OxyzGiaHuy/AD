# Run ablation_alpha_0p5_mvtec_toothbrush_k4_seed3_head_pca_k4_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p5_mvtec_toothbrush_k4_seed3.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9865382661118663`
- `auroc`: `0.9638888888888889`
- `brier`: `0.20489261631372685`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.08269280904815313`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0057311684691480225`
- `max_f1`: `0.9508196721311475`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6006031797572338`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_alpha_0p5_mvtec_toothbrush_k4_seed3_head_pca_k4_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
