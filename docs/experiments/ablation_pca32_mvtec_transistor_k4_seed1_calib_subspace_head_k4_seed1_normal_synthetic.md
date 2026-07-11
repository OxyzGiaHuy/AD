# Run ablation_pca32_mvtec_transistor_k4_seed1_calib_subspace_head_k4_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca32_mvtec_transistor_k4_seed1.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.768385963560035`
- `auroc`: `0.8204166666666667`
- `brier`: `0.24969203781891278`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.275813242712066`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.002171575929969549`
- `max_f1`: `0.7021276595744681`
- `model_storage_mb`: `0.4253120422363281`
- `nll`: `0.9770705158373206`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_pca32_mvtec_transistor_k4_seed1_calib_subspace_head_k4_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
