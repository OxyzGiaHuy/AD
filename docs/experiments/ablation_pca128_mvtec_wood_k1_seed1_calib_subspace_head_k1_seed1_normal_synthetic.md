# Run ablation_pca128_mvtec_wood_k1_seed1_calib_subspace_head_k1_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca128_mvtec_wood_k1_seed1.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9450571853804229`
- `auroc`: `0.8587719298245614`
- `brier`: `0.238027570555755`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.23923030533368073`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0030868864747919614`
- `max_f1`: `0.9302325581395349`
- `model_storage_mb`: `0.5659370422363281`
- `nll`: `2.034780834759145`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_pca128_mvtec_wood_k1_seed1_calib_subspace_head_k1_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
