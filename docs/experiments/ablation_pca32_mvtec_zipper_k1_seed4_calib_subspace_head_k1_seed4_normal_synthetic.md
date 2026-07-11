# Run ablation_pca32_mvtec_zipper_k1_seed4_calib_subspace_head_k1_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca32_mvtec_zipper_k1_seed4.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9855341568490539`
- `auroc`: `0.9464285714285714`
- `brier`: `0.20349774025589018`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.20739369755549145`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.00222076993707`
- `max_f1`: `0.9508196721311475`
- `model_storage_mb`: `0.4253120422363281`
- `nll`: `1.439000713126951`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_pca32_mvtec_zipper_k1_seed4_calib_subspace_head_k1_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
