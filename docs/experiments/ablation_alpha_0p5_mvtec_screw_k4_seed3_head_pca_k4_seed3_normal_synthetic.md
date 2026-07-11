# Run ablation_alpha_0p5_mvtec_screw_k4_seed3_head_pca_k4_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p5_mvtec_screw_k4_seed3.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.8557574430323562`
- `auroc`: `0.7335519573683131`
- `brier`: `0.2000751233269873`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.16608081907033923`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0019038690603338181`
- `max_f1`: `0.8784313725490196`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.5911412268272235`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_alpha_0p5_mvtec_screw_k4_seed3_head_pca_k4_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
