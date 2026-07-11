# Run ablation_pca16_mvtec_carpet_k1_seed3_calib_subspace_head_k1_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca16_mvtec_carpet_k1_seed3.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9988757132041219`
- `auroc`: `0.9963884430176565`
- `brier`: `0.14891617774530116`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.16577783850634575`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.002832885465433455`
- `max_f1`: `0.9834254143646409`
- `model_storage_mb`: `0.4018745422363281`
- `nll`: `0.9322415022462311`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_pca16_mvtec_carpet_k1_seed3_calib_subspace_head_k1_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
