# Run ablation_pca16_mvtec_transistor_k1_seed1_calib_subspace_head_k1_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca16_mvtec_transistor_k1_seed1.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.7291841512029272`
- `auroc`: `0.79625`
- `brier`: `0.27141616937185237`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.27891424076166005`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.001441815085709095`
- `max_f1`: `0.7083333333333334`
- `model_storage_mb`: `0.4018745422363281`
- `nll`: `1.3901461626667375`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_pca16_mvtec_transistor_k1_seed1_calib_subspace_head_k1_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
