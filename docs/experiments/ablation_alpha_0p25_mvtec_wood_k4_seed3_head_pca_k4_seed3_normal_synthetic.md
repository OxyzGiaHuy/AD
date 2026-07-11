# Run ablation_alpha_0p25_mvtec_wood_k4_seed3_head_pca_k4_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p25_mvtec_wood_k4_seed3.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9897766764709676`
- `auroc`: `0.9719298245614035`
- `brier`: `0.215171949453528`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.3980558152440227`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0030602515922694266`
- `max_f1`: `0.967741935483871`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6232147150299897`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_alpha_0p25_mvtec_wood_k4_seed3_head_pca_k4_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
