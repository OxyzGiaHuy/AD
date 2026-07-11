# Run ablation_alpha_1p0_mvtec_grid_k1_seed2_head_pca_k1_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_1p0_mvtec_grid_k1_seed2.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.873322401805644`
- `auroc`: `0.7543859649122807`
- `brier`: `0.19184097030651684`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.043111558908071224`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.003170898876702174`
- `max_f1`: `0.875`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.5709510842798178`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_alpha_1p0_mvtec_grid_k1_seed2_head_pca_k1_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
