# Run ablation_pca32_mvtec_carpet_k4_seed0_calib_subspace_head_k4_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca32_mvtec_carpet_k4_seed0.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9982366998938913`
- `auroc`: `0.9943820224719101`
- `brier`: `0.11361321339184098`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.13417294691515783`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0014866024860714236`
- `max_f1`: `0.9834254143646409`
- `model_storage_mb`: `0.4253120422363281`
- `nll`: `0.6299947767619687`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_pca32_mvtec_carpet_k4_seed0_calib_subspace_head_k4_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
