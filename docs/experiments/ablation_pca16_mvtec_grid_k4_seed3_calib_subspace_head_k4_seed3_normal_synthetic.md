# Run ablation_pca16_mvtec_grid_k4_seed3_calib_subspace_head_k4_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca16_mvtec_grid_k4_seed3.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9820627173175508`
- `auroc`: `0.949874686716792`
- `brier`: `0.08518104995833549`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.1040126436855644`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0031338568585805404`
- `max_f1`: `0.9272727272727272`
- `model_storage_mb`: `0.4018745422363281`
- `nll`: `0.26678106885837194`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_pca16_mvtec_grid_k4_seed3_calib_subspace_head_k4_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
