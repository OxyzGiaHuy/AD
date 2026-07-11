# Run ablation_pca128_mvtec_toothbrush_k4_seed3_calib_subspace_head_k4_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca128_mvtec_toothbrush_k4_seed3.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9805205445363492`
- `auroc`: `0.9527777777777777`
- `brier`: `0.24429276411303197`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.25770849202360424`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.003515733627691155`
- `max_f1`: `0.9523809523809523`
- `model_storage_mb`: `0.5659370422363281`
- `nll`: `2.032087065884589`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_pca128_mvtec_toothbrush_k4_seed3_calib_subspace_head_k4_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
