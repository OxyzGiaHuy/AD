# Run ablation_alpha_0p5_mvtec_toothbrush_k1_seed3_head_pca_k1_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p5_mvtec_toothbrush_k1_seed3.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9673139394871029`
- `auroc`: `0.9166666666666666`
- `brier`: `0.20935199890446882`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.09581818892842253`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0019839999842501824`
- `max_f1`: `0.9206349206349206`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6102453325658158`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_alpha_0p5_mvtec_toothbrush_k1_seed3_head_pca_k1_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
