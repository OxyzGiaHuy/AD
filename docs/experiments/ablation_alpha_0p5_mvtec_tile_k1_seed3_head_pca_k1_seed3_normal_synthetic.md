# Run ablation_alpha_0p5_mvtec_tile_k1_seed3_head_pca_k1_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p5_mvtec_tile_k1_seed3.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9779337667222341`
- `auroc`: `0.9329004329004329`
- `brier`: `0.20821422782021953`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.35642842706452066`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.002180785434240969`
- `max_f1`: `0.9341317365269461`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6080383481298836`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_alpha_0p5_mvtec_tile_k1_seed3_head_pca_k1_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
