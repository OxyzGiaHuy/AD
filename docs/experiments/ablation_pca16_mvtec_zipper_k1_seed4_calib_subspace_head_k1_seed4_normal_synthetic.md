# Run ablation_pca16_mvtec_zipper_k1_seed4_calib_subspace_head_k1_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca16_mvtec_zipper_k1_seed4.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9840693015991047`
- `auroc`: `0.9438025210084033`
- `brier`: `0.07892650430199144`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.08118918307421621`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0021204388644916333`
- `max_f1`: `0.9477911646586346`
- `model_storage_mb`: `0.4018745422363281`
- `nll`: `0.3141515423215934`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_pca16_mvtec_zipper_k1_seed4_calib_subspace_head_k1_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
