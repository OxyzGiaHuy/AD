# Run ablation_pca64_mvtec_carpet_k1_seed2_calib_subspace_head_k1_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca64_mvtec_carpet_k1_seed2.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.99810197760602`
- `auroc`: `0.9939807383627608`
- `brier`: `0.2141375300103488`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.22510906773754677`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0021078278684717976`
- `max_f1`: `0.9834254143646409`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `1.3267154829040761`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_pca64_mvtec_carpet_k1_seed2_calib_subspace_head_k1_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
