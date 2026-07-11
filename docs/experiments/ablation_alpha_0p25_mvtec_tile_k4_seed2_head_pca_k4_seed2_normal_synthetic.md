# Run ablation_alpha_0p25_mvtec_tile_k4_seed2_head_pca_k4_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p25_mvtec_tile_k4_seed2.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9893992134469162`
- `auroc`: `0.9747474747474747`
- `brier`: `0.22049939263108764`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.368681958088508`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.002791082741230981`
- `max_f1`: `0.9710982658959537`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6339176439449207`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_alpha_0p25_mvtec_tile_k4_seed2_head_pca_k4_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
