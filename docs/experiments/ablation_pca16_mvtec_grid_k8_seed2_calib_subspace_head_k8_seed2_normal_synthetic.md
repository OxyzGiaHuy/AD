# Run ablation_pca16_mvtec_grid_k8_seed2_calib_subspace_head_k8_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca16_mvtec_grid_k8_seed2.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9956387578463792`
- `auroc`: `0.9874686716791979`
- `brier`: `0.19507913141477778`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.18988625284952992`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0037712538137267796`
- `max_f1`: `0.9642857142857143`
- `model_storage_mb`: `0.4018745422363281`
- `nll`: `0.5857911644419277`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_pca16_mvtec_grid_k8_seed2_calib_subspace_head_k8_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
