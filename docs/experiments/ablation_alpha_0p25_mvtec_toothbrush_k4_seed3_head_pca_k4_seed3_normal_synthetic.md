# Run ablation_alpha_0p25_mvtec_toothbrush_k4_seed3_head_pca_k4_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p25_mvtec_toothbrush_k4_seed3.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9873319169055172`
- `auroc`: `0.9666666666666667`
- `brier`: `0.21680147329936947`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.14777903755505883`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.002635577782278969`
- `max_f1`: `0.9508196721311475`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6261691658140942`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_alpha_0p25_mvtec_toothbrush_k4_seed3_head_pca_k4_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
