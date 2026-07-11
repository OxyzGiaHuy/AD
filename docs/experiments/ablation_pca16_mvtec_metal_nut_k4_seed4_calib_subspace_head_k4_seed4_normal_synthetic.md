# Run ablation_pca16_mvtec_metal_nut_k4_seed4_calib_subspace_head_k4_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca16_mvtec_metal_nut_k4_seed4.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9279107858315093`
- `auroc`: `0.7932551319648093`
- `brier`: `0.1254151942330778`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.11738355056099274`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0015760124539551527`
- `max_f1`: `0.9285714285714286`
- `model_storage_mb`: `0.4018745422363281`
- `nll`: `0.4662451858650976`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_pca16_mvtec_metal_nut_k4_seed4_calib_subspace_head_k4_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
