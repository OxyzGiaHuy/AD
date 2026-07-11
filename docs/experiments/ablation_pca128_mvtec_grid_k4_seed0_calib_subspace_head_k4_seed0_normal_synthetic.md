# Run ablation_pca128_mvtec_grid_k4_seed0_calib_subspace_head_k4_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca128_mvtec_grid_k4_seed0.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9936343088365229`
- `auroc`: `0.9832915622389307`
- `brier`: `0.25015857876039205`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.25789075478529316`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0032869622063560365`
- `max_f1`: `0.9739130434782609`
- `model_storage_mb`: `0.5659370422363281`
- `nll`: `1.908929777246654`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_pca128_mvtec_grid_k4_seed0_calib_subspace_head_k4_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
