# Run ablation_pca32_mvtec_zipper_k1_seed2_calib_subspace_head_k1_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca32_mvtec_zipper_k1_seed2.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9866459972728143`
- `auroc`: `0.9522058823529411`
- `brier`: `0.1921948737214227`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.19669589326279052`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.004320196548341126`
- `max_f1`: `0.9444444444444444`
- `model_storage_mb`: `0.4253120422363281`
- `nll`: `2.2034161589676655`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_pca32_mvtec_zipper_k1_seed2_calib_subspace_head_k1_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
