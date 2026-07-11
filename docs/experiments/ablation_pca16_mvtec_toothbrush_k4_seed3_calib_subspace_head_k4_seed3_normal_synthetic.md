# Run ablation_pca16_mvtec_toothbrush_k4_seed3_calib_subspace_head_k4_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca16_mvtec_toothbrush_k4_seed3.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9777812401416405`
- `auroc`: `0.9416666666666667`
- `brier`: `0.11557761111164457`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.14943953324109316`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0044382597275433085`
- `max_f1`: `0.9206349206349206`
- `model_storage_mb`: `0.4018745422363281`
- `nll`: `0.46930558153384494`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_pca16_mvtec_toothbrush_k4_seed3_calib_subspace_head_k4_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
