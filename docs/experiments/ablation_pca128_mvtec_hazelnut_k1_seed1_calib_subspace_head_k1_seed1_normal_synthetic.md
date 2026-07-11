# Run ablation_pca128_mvtec_hazelnut_k1_seed1_calib_subspace_head_k1_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca128_mvtec_hazelnut_k1_seed1.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9775690378533191`
- `auroc`: `0.9557142857142857`
- `brier`: `0.36356518440601077`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.3635995127938011`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0018334024839780547`
- `max_f1`: `0.9078014184397163`
- `model_storage_mb`: `0.5659370422363281`
- `nll`: `3.847425250541885`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_pca128_mvtec_hazelnut_k1_seed1_calib_subspace_head_k1_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
