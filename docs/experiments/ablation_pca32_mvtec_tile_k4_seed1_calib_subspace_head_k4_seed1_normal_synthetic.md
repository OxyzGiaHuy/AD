# Run ablation_pca32_mvtec_tile_k4_seed1_calib_subspace_head_k4_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca32_mvtec_tile_k4_seed1.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9890481369627976`
- `auroc`: `0.9736652236652237`
- `brier`: `0.19354385794025017`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.20642982028488424`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.002544269809483463`
- `max_f1`: `0.9540229885057471`
- `model_storage_mb`: `0.4253120422363281`
- `nll`: `0.5675893060497129`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_pca32_mvtec_tile_k4_seed1_calib_subspace_head_k4_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
