# Run ablation_pca128_mvtec_transistor_k1_seed0_calib_subspace_head_k1_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca128_mvtec_transistor_k1_seed0.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.8092130402371452`
- `auroc`: `0.8420833333333333`
- `brier`: `0.5982585391515041`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.5990516185760498`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0015470676310360431`
- `max_f1`: `0.7317073170731707`
- `model_storage_mb`: `0.5659370422363281`
- `nll`: `4.588725650691776`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_pca128_mvtec_transistor_k1_seed0_calib_subspace_head_k1_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
