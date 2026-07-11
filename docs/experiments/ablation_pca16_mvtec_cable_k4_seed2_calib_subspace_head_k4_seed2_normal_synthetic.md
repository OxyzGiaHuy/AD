# Run ablation_pca16_mvtec_cable_k4_seed2_calib_subspace_head_k4_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca16_mvtec_cable_k4_seed2.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9219020683522925`
- `auroc`: `0.8620689655172413`
- `brier`: `0.18396916797519378`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.18409054589419008`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0013608310371637344`
- `max_f1`: `0.8279569892473119`
- `model_storage_mb`: `0.4018745422363281`
- `nll`: `0.7004340861436951`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_pca16_mvtec_cable_k4_seed2_calib_subspace_head_k4_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
