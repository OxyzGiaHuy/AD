# Run ablation_pca128_mvtec_pill_k1_seed1_calib_subspace_head_k1_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca128_mvtec_pill_k1_seed1.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9861225093079232`
- `auroc`: `0.9323513366066557`
- `brier`: `0.15435901533333185`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.15495573938963658`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.004843651177640447`
- `max_f1`: `0.9574468085106383`
- `model_storage_mb`: `0.5659370422363281`
- `nll`: `1.1217137188522484`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_pca128_mvtec_pill_k1_seed1_calib_subspace_head_k1_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
