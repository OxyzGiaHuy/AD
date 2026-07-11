# Run ablation_pca64_mvtec_toothbrush_k1_seed3_calib_subspace_head_k1_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca64_mvtec_toothbrush_k1_seed3.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9835788218296043`
- `auroc`: `0.9583333333333334`
- `brier`: `0.2855460338892725`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.28563002887226285`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.002460720017552376`
- `max_f1`: `0.9375`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `3.840947591868286`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_pca64_mvtec_toothbrush_k1_seed3_calib_subspace_head_k1_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
