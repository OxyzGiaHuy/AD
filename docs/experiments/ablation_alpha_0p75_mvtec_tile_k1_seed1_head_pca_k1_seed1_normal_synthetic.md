# Run ablation_alpha_0p75_mvtec_tile_k1_seed1_head_pca_k1_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p75_mvtec_tile_k1_seed1.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9706769000111622`
- `auroc`: `0.913059163059163`
- `brier`: `0.19859212149968122`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.24747238964097112`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0027127060561608044`
- `max_f1`: `0.9044585987261147`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.5866477654921844`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_alpha_0p75_mvtec_tile_k1_seed1_head_pca_k1_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
