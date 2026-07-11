# Run ablation_pca32_mvtec_capsule_k4_seed3_calib_subspace_head_k4_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca32_mvtec_capsule_k4_seed3.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9253754156348957`
- `auroc`: `0.7614678899082569`
- `brier`: `0.11865949299403433`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.09744405198955174`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0015637857670133765`
- `max_f1`: `0.9321266968325792`
- `model_storage_mb`: `0.4253120422363281`
- `nll`: `0.4695241498133938`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_pca32_mvtec_capsule_k4_seed3_calib_subspace_head_k4_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
