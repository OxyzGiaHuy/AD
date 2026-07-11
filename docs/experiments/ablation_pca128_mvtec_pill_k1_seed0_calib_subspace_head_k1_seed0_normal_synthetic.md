# Run ablation_pca128_mvtec_pill_k1_seed0_calib_subspace_head_k1_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca128_mvtec_pill_k1_seed0.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9839795294196733`
- `auroc`: `0.9206219312602292`
- `brier`: `0.15446842067360814`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.15496815321688162`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.002161963089943646`
- `max_f1`: `0.9494949494949495`
- `model_storage_mb`: `0.5659370422363281`
- `nll`: `1.0877331764532665`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_pca128_mvtec_pill_k1_seed0_calib_subspace_head_k1_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
