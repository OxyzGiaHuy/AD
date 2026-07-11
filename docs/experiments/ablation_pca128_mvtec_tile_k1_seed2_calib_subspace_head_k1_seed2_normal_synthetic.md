# Run ablation_pca128_mvtec_tile_k1_seed2_calib_subspace_head_k1_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca128_mvtec_tile_k1_seed2.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9921055827087555`
- `auroc`: `0.9812409812409812`
- `brier`: `0.27260953707679497`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.27690423808546144`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.002461908385157585`
- `max_f1`: `0.9655172413793104`
- `model_storage_mb`: `0.5659370422363281`
- `nll`: `1.614313385204324`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_pca128_mvtec_tile_k1_seed2_calib_subspace_head_k1_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
