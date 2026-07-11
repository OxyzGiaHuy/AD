# Run ablation_pca16_mvtec_cable_k4_seed4_calib_subspace_head_k4_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca16_mvtec_cable_k4_seed4.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.8521296410172722`
- `auroc`: `0.7747376311844077`
- `brier`: `0.24698256350160241`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.23908722338529592`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.00171833124011755`
- `max_f1`: `0.7924528301886793`
- `model_storage_mb`: `0.4018745422363281`
- `nll`: `1.132851688803982`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_pca16_mvtec_cable_k4_seed4_calib_subspace_head_k4_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
