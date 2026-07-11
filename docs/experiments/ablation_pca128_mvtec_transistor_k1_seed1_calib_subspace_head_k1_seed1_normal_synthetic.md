# Run ablation_pca128_mvtec_transistor_k1_seed1_calib_subspace_head_k1_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca128_mvtec_transistor_k1_seed1.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9132761077490255`
- `auroc`: `0.9358333333333333`
- `brier`: `0.595029238058835`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.5974411875009537`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0029099109768867494`
- `max_f1`: `0.8333333333333334`
- `model_storage_mb`: `0.5659370422363281`
- `nll`: `3.926325455913701`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_pca128_mvtec_transistor_k1_seed1_calib_subspace_head_k1_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
