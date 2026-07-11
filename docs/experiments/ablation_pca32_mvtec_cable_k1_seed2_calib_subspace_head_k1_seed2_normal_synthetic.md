# Run ablation_pca32_mvtec_cable_k1_seed2_calib_subspace_head_k1_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca32_mvtec_cable_k1_seed2.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9378629472351065`
- `auroc`: `0.8826836581709145`
- `brier`: `0.386289738028238`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.3864725458621979`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0016922280316551527`
- `max_f1`: `0.8651685393258427`
- `model_storage_mb`: `0.4253120422363281`
- `nll`: `4.951436742075163`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_pca32_mvtec_cable_k1_seed2_calib_subspace_head_k1_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
