# Run ablation_pca16_mvtec_pill_k4_seed3_calib_subspace_head_k4_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca16_mvtec_pill_k4_seed3.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9745831259914998`
- `auroc`: `0.8753409710856519`
- `brier`: `0.08815834503626634`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.06889681451156474`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.002225581712708502`
- `max_f1`: `0.9427609427609428`
- `model_storage_mb`: `0.4018745422363281`
- `nll`: `0.30000370100212836`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_pca16_mvtec_pill_k4_seed3_calib_subspace_head_k4_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
