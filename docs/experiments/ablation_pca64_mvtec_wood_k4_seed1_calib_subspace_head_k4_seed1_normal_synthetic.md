# Run ablation_pca64_mvtec_wood_k4_seed1_calib_subspace_head_k4_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca64_mvtec_wood_k4_seed1.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9817318703120719`
- `auroc`: `0.95`
- `brier`: `0.19806733714692484`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.21481132582773133`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0019215591063227835`
- `max_f1`: `0.959349593495935`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `1.5124959538480225`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_pca64_mvtec_wood_k4_seed1_calib_subspace_head_k4_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
