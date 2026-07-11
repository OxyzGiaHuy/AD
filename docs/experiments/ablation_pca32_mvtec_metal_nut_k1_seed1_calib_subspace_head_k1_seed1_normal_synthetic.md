# Run ablation_pca32_mvtec_metal_nut_k1_seed1_calib_subspace_head_k1_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca32_mvtec_metal_nut_k1_seed1.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9589751110749091`
- `auroc`: `0.852394916911046`
- `brier`: `0.18536453901388014`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.18792049003684003`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.001644966265429621`
- `max_f1`: `0.9333333333333333`
- `model_storage_mb`: `0.4253120422363281`
- `nll`: `2.6609923360431638`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_pca32_mvtec_metal_nut_k1_seed1_calib_subspace_head_k1_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
