# Run ablation_alpha_1p0_mvtec_carpet_k1_seed2_head_pca_k1_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_1p0_mvtec_carpet_k1_seed2.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9707357682950872`
- `auroc`: `0.9157303370786517`
- `brier`: `0.1736651287702506`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.16972058400129658`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.002519361674785614`
- `max_f1`: `0.9325842696629213`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.5320870409225115`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_alpha_1p0_mvtec_carpet_k1_seed2_head_pca_k1_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
