# Run ablation_pca32_mvtec_grid_k1_seed1_calib_subspace_head_k1_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca32_mvtec_grid_k1_seed1.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9412378871987497`
- `auroc`: `0.8813700918964077`
- `brier`: `0.2663458398782167`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.2676971738155072`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0014056816267279477`
- `max_f1`: `0.9411764705882353`
- `model_storage_mb`: `0.4253120422363281`
- `nll`: `4.522011842350841`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_pca32_mvtec_grid_k1_seed1_calib_subspace_head_k1_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
