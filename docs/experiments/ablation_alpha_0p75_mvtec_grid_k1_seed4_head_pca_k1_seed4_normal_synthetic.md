# Run ablation_alpha_0p75_mvtec_grid_k1_seed4_head_pca_k1_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p75_mvtec_grid_k1_seed4.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9732538480489206`
- `auroc`: `0.9214703425229741`
- `brier`: `0.19851737630979147`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.07473922922061044`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.003813776832360488`
- `max_f1`: `0.9272727272727272`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.5867844101643674`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_alpha_0p75_mvtec_grid_k1_seed4_head_pca_k1_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
