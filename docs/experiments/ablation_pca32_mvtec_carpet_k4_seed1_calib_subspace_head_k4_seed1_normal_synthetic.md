# Run ablation_pca32_mvtec_carpet_k4_seed1_calib_subspace_head_k4_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca32_mvtec_carpet_k4_seed1.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9982428140864124`
- `auroc`: `0.9943820224719101`
- `brier`: `0.10092129535805905`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.12677121014358136`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0016930729914934207`
- `max_f1`: `0.9834254143646409`
- `model_storage_mb`: `0.4253120422363281`
- `nll`: `0.6017786546066931`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_pca32_mvtec_carpet_k4_seed1_calib_subspace_head_k4_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
