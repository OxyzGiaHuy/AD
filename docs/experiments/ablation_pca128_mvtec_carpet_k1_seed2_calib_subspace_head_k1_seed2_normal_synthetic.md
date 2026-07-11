# Run ablation_pca128_mvtec_carpet_k1_seed2_calib_subspace_head_k1_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca128_mvtec_carpet_k1_seed2.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9986177684667286`
- `auroc`: `0.9955858747993579`
- `brier`: `0.1853841851287935`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.20810552641876745`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0017934924739803004`
- `max_f1`: `0.9834254143646409`
- `model_storage_mb`: `0.5659370422363281`
- `nll`: `0.8358292451667927`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_pca128_mvtec_carpet_k1_seed2_calib_subspace_head_k1_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
