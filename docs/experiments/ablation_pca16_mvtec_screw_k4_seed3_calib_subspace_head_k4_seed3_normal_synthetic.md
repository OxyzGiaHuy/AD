# Run ablation_pca16_mvtec_screw_k4_seed3_calib_subspace_head_k4_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca16_mvtec_screw_k4_seed3.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.8146466090094976`
- `auroc`: `0.586185693789711`
- `brier`: `0.44903697059002284`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.465056534126461`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0019809631048701704`
- `max_f1`: `0.8530465949820788`
- `model_storage_mb`: `0.4018745422363281`
- `nll`: `1.7669764202796254`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_pca16_mvtec_screw_k4_seed3_calib_subspace_head_k4_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
