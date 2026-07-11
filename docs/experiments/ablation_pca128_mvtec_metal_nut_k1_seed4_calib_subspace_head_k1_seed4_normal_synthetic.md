# Run ablation_pca128_mvtec_metal_nut_k1_seed4_calib_subspace_head_k1_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca128_mvtec_metal_nut_k1_seed4.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9935595583266641`
- `auroc`: `0.9736070381231672`
- `brier`: `0.18749623434242726`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.18932803713757063`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.002399043188146923`
- `max_f1`: `0.9633507853403142`
- `model_storage_mb`: `0.5659370422363281`
- `nll`: `1.1781320005946896`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_pca128_mvtec_metal_nut_k1_seed4_calib_subspace_head_k1_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
