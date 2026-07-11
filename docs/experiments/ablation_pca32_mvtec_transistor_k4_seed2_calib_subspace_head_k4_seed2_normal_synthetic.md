# Run ablation_pca32_mvtec_transistor_k4_seed2_calib_subspace_head_k4_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca32_mvtec_transistor_k4_seed2.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.7898198685056059`
- `auroc`: `0.83`
- `brier`: `0.2971451237618169`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.3242611139640212`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0014578279294073582`
- `max_f1`: `0.7021276595744681`
- `model_storage_mb`: `0.4253120422363281`
- `nll`: `1.1995342511285998`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_pca32_mvtec_transistor_k4_seed2_calib_subspace_head_k4_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
