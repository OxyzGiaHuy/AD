# Run ablation_pca32_mvtec_leather_k4_seed2_calib_subspace_head_k4_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca32_mvtec_leather_k4_seed2.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9992882365421916`
- `auroc`: `0.9979619565217391`
- `brier`: `0.18118108529869442`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.19828898880270213`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.002657054593005488`
- `max_f1`: `0.989247311827957`
- `model_storage_mb`: `0.4253120422363281`
- `nll`: `0.6116451150411076`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_pca32_mvtec_leather_k4_seed2_calib_subspace_head_k4_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
