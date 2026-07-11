# Run ablation_pca32_mvtec_toothbrush_k4_seed0_calib_subspace_head_k4_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca32_mvtec_toothbrush_k4_seed0.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9791677384503837`
- `auroc`: `0.9444444444444444`
- `brier`: `0.2093807581937939`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.2232962431652205`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.002894179274638494`
- `max_f1`: `0.9180327868852459`
- `model_storage_mb`: `0.4253120422363281`
- `nll`: `0.7255960125341446`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_pca32_mvtec_toothbrush_k4_seed0_calib_subspace_head_k4_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
