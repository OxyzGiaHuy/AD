# Run ablation_pca32_mvtec_toothbrush_k1_seed2_calib_subspace_head_k1_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca32_mvtec_toothbrush_k1_seed2.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9667600505678505`
- `auroc`: `0.9111111111111111`
- `brier`: `0.20690992508914827`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.21042167870438702`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0018292713378156935`
- `max_f1`: `0.90625`
- `model_storage_mb`: `0.4253120422363281`
- `nll`: `3.116524327712249`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_pca32_mvtec_toothbrush_k1_seed2_calib_subspace_head_k1_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
