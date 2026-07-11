# Run ablation_pca128_mvtec_zipper_k1_seed1_calib_subspace_head_k1_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca128_mvtec_zipper_k1_seed1.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9814288157666882`
- `auroc`: `0.9356617647058824`
- `brier`: `0.1954051369877236`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.20231868849684853`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.001473048467509794`
- `max_f1`: `0.952`
- `model_storage_mb`: `0.5659370422363281`
- `nll`: `1.0296714561834823`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_pca128_mvtec_zipper_k1_seed1_calib_subspace_head_k1_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
