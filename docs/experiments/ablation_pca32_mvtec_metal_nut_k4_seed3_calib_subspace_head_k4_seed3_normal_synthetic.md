# Run ablation_pca32_mvtec_metal_nut_k4_seed3_calib_subspace_head_k4_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca32_mvtec_metal_nut_k4_seed3.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9721524779506464`
- `auroc`: `0.9027370478983382`
- `brier`: `0.14222660696830564`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.14902710681376252`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0015052043711361678`
- `max_f1`: `0.9435897435897436`
- `model_storage_mb`: `0.4253120422363281`
- `nll`: `0.5389437588009603`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_pca32_mvtec_metal_nut_k4_seed3_calib_subspace_head_k4_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
