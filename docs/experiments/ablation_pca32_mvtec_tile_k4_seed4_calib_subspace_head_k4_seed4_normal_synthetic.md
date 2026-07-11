# Run ablation_pca32_mvtec_tile_k4_seed4_calib_subspace_head_k4_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca32_mvtec_tile_k4_seed4.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9923791169966595`
- `auroc`: `0.9819624819624819`
- `brier`: `0.12106530021760238`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.16596996121936375`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0025753239567717933`
- `max_f1`: `0.9710982658959537`
- `model_storage_mb`: `0.4253120422363281`
- `nll`: `0.38351120867708893`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_pca32_mvtec_tile_k4_seed4_calib_subspace_head_k4_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
