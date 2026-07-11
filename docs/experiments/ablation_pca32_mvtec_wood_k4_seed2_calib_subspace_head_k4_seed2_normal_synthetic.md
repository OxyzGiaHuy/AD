# Run ablation_pca32_mvtec_wood_k4_seed2_calib_subspace_head_k4_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca32_mvtec_wood_k4_seed2.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9796907923682275`
- `auroc`: `0.9377192982456141`
- `brier`: `0.19181212920416466`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.19732721951566173`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.002771904385542568`
- `max_f1`: `0.9375`
- `model_storage_mb`: `0.4253120422363281`
- `nll`: `0.8422184002454627`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_pca32_mvtec_wood_k4_seed2_calib_subspace_head_k4_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
