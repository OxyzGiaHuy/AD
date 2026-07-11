# Run ablation_alpha_0p25_mvtec_transistor_k4_seed3_head_pca_k4_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p25_mvtec_transistor_k4_seed3.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.823138364648057`
- `auroc`: `0.8895833333333333`
- `brier`: `0.25194851625675924`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.14884348511695866`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0037299242056906224`
- `max_f1`: `0.7872340425531915`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6969489359013994`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_alpha_0p25_mvtec_transistor_k4_seed3_head_pca_k4_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
