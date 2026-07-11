# Run ablation_pca128_mvtec_pill_k4_seed4_calib_subspace_head_k4_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca128_mvtec_pill_k4_seed4.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9850732231519747`
- `auroc`: `0.9356246590289143`
- `brier`: `0.09694998270116467`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.11491419557861222`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.001573478089210516`
- `max_f1`: `0.968421052631579`
- `model_storage_mb`: `0.5659370422363281`
- `nll`: `0.4583547624338031`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_pca128_mvtec_pill_k4_seed4_calib_subspace_head_k4_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
