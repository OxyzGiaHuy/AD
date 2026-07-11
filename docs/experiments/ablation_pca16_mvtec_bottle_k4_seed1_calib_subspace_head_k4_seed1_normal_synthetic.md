# Run ablation_pca16_mvtec_bottle_k4_seed1_calib_subspace_head_k4_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca16_mvtec_bottle_k4_seed1.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9494109817794183`
- `auroc`: `0.9079365079365079`
- `brier`: `0.07532777399197654`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.07409106436780237`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0027534086481634393`
- `max_f1`: `0.9402985074626866`
- `model_storage_mb`: `0.4018745422363281`
- `nll`: `0.2902754926900525`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_pca16_mvtec_bottle_k4_seed1_calib_subspace_head_k4_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
