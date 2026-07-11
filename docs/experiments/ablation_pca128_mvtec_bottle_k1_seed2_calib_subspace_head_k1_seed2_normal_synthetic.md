# Run ablation_pca128_mvtec_bottle_k1_seed2_calib_subspace_head_k1_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca128_mvtec_bottle_k1_seed2.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9717377403978937`
- `auroc`: `0.9142857142857143`
- `brier`: `0.23968615902749182`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.24030424026121577`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.002574731741684029`
- `max_f1`: `0.9264705882352942`
- `model_storage_mb`: `0.5659370422363281`
- `nll`: `2.051204798269252`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_pca128_mvtec_bottle_k1_seed2_calib_subspace_head_k1_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
