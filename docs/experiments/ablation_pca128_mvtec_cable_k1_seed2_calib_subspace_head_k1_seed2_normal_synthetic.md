# Run ablation_pca128_mvtec_cable_k1_seed2_calib_subspace_head_k1_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca128_mvtec_cable_k1_seed2.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.910820396117401`
- `auroc`: `0.8467016491754122`
- `brier`: `0.3864314521039584`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.38653059720993044`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0015589878956476847`
- `max_f1`: `0.83`
- `model_storage_mb`: `0.5659370422363281`
- `nll`: `3.8627162057331814`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_pca128_mvtec_cable_k1_seed2_calib_subspace_head_k1_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
