# Run ablation_pca64_mvtec_bottle_k4_seed2_calib_subspace_head_k4_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca64_mvtec_bottle_k4_seed2.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9946595511607746`
- `auroc`: `0.984920634920635`
- `brier`: `0.12192627250534865`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.15301327344523857`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0029654207089579248`
- `max_f1`: `0.984375`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `0.5627530220517767`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_pca64_mvtec_bottle_k4_seed2_calib_subspace_head_k4_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
