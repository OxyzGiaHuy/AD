# Run ablation_pca128_mvtec_toothbrush_k4_seed2_calib_subspace_head_k4_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca128_mvtec_toothbrush_k4_seed2.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9811641988211325`
- `auroc`: `0.9555555555555556`
- `brier`: `0.22636295914807097`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.2484344428493863`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.003756672321330933`
- `max_f1`: `0.967741935483871`
- `model_storage_mb`: `0.5659370422363281`
- `nll`: `1.4564941542679022`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_pca128_mvtec_toothbrush_k4_seed2_calib_subspace_head_k4_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
