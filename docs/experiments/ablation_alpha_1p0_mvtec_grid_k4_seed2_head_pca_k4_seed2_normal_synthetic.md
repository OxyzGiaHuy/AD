# Run ablation_alpha_1p0_mvtec_grid_k4_seed2_head_pca_k4_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_1p0_mvtec_grid_k4_seed2.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9823984564166708`
- `auroc`: `0.9536340852130326`
- `brier`: `0.1945816983021335`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.02273246263846377`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.002436117484019353`
- `max_f1`: `0.9369369369369369`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.5770421572527977`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_alpha_1p0_mvtec_grid_k4_seed2_head_pca_k4_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
