# Run ablation_pca128_mvtec_wood_k4_seed0_calib_subspace_head_k4_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca128_mvtec_wood_k4_seed0.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9849910057041829`
- `auroc`: `0.9552631578947368`
- `brier`: `0.19111989268411492`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.21124094271961652`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.002120183639322655`
- `max_f1`: `0.943089430894309`
- `model_storage_mb`: `0.5659370422363281`
- `nll`: `1.2286218912808706`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_pca128_mvtec_wood_k4_seed0_calib_subspace_head_k4_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
