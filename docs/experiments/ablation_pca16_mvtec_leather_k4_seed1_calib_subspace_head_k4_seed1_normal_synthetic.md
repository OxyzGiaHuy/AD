# Run ablation_pca16_mvtec_leather_k4_seed1_calib_subspace_head_k4_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca16_mvtec_leather_k4_seed1.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9855281106992184`
- `auroc`: `0.9609375`
- `brier`: `0.20233636105209726`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.17091654998160175`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0023521129492550127`
- `max_f1`: `0.9528795811518325`
- `model_storage_mb`: `0.4018745422363281`
- `nll`: `0.6246161126106039`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_pca16_mvtec_leather_k4_seed1_calib_subspace_head_k4_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
