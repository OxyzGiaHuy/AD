# Run ablation_pca32_mvtec_toothbrush_k4_seed1_calib_subspace_head_k4_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca32_mvtec_toothbrush_k4_seed1.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9823531810356523`
- `auroc`: `0.9555555555555556`
- `brier`: `0.15510722975639654`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.17863526975824714`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0039393578966458636`
- `max_f1`: `0.9354838709677419`
- `model_storage_mb`: `0.4253120422363281`
- `nll`: `1.027164133377791`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_pca32_mvtec_toothbrush_k4_seed1_calib_subspace_head_k4_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
