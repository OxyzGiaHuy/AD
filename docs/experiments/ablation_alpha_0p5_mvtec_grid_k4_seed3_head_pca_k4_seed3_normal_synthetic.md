# Run ablation_alpha_0p5_mvtec_grid_k4_seed3_head_pca_k4_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p5_mvtec_grid_k4_seed3.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.999097505881862`
- `auroc`: `0.9974937343358395`
- `brier`: `0.20622075139007434`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.4046216072180333`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.004504219796030949`
- `max_f1`: `0.9827586206896551`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6041264039909681`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_alpha_0p5_mvtec_grid_k4_seed3_head_pca_k4_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
