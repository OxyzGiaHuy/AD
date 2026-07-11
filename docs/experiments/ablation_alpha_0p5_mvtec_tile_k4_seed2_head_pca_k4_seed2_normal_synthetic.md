# Run ablation_alpha_0p5_mvtec_tile_k4_seed2_head_pca_k4_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p5_mvtec_tile_k4_seed2.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9892743695018476`
- `auroc`: `0.9743867243867244`
- `brier`: `0.20137881588548515`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.3774941945687319`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.002555116135467831`
- `max_f1`: `0.9655172413793104`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.59393231154043`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_alpha_0p5_mvtec_tile_k4_seed2_head_pca_k4_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
