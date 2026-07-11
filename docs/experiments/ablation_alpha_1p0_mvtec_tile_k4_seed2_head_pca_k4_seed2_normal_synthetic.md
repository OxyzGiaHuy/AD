# Run ablation_alpha_1p0_mvtec_tile_k4_seed2_head_pca_k4_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_1p0_mvtec_tile_k4_seed2.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9701074979391829`
- `auroc`: `0.9485930735930735`
- `brier`: `0.1901333267734898`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.1240807893948677`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0019262456295327244`
- `max_f1`: `0.9651162790697675`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.564791171584302`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_alpha_1p0_mvtec_tile_k4_seed2_head_pca_k4_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
