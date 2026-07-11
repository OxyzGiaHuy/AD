# Run ablation_pca64_mvtec_carpet_k4_seed3_calib_subspace_head_k4_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca64_mvtec_carpet_k4_seed3.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9970658085348822`
- `auroc`: `0.9907704654895666`
- `brier`: `0.09667184623526417`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.11471810264703944`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0018629295608172049`
- `max_f1`: `0.978021978021978`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `0.7422996860690263`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_pca64_mvtec_carpet_k4_seed3_calib_subspace_head_k4_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
