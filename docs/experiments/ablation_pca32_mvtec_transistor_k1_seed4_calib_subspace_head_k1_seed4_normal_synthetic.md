# Run ablation_pca32_mvtec_transistor_k1_seed4_calib_subspace_head_k1_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca32_mvtec_transistor_k1_seed4.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.7703715157831477`
- `auroc`: `0.80875`
- `brier`: `0.45802482325411586`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.49676044382154944`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0014333560690283776`
- `max_f1`: `0.693069306930693`
- `model_storage_mb`: `0.4253120422363281`
- `nll`: `2.676424517591207`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_pca32_mvtec_transistor_k1_seed4_calib_subspace_head_k1_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
