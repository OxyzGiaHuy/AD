# Run ablation_pca32_mvtec_grid_k8_seed4_calib_subspace_head_k8_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca32_mvtec_grid_k8_seed4.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.999697519661222`
- `auroc`: `0.9991645781119465`
- `brier`: `0.18168699947853545`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.20348924990647882`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0029809543958459147`
- `max_f1`: `0.991304347826087`
- `model_storage_mb`: `0.4253120422363281`
- `nll`: `0.512595138807209`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_pca32_mvtec_grid_k8_seed4_calib_subspace_head_k8_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
