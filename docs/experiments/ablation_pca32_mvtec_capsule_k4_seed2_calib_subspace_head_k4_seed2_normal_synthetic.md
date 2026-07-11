# Run ablation_pca32_mvtec_capsule_k4_seed2_calib_subspace_head_k4_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca32_mvtec_capsule_k4_seed2.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.8899436239073013`
- `auroc`: `0.6836856800957319`
- `brier`: `0.138151195132403`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.11576642999143313`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0018377033146944914`
- `max_f1`: `0.927038626609442`
- `model_storage_mb`: `0.4253120422363281`
- `nll`: `0.46619885107518677`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_pca32_mvtec_capsule_k4_seed2_calib_subspace_head_k4_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
