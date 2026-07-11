# Run ablation_pca16_mvtec_toothbrush_k4_seed4_calib_subspace_head_k4_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca16_mvtec_toothbrush_k4_seed4.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.982776497016764`
- `auroc`: `0.9555555555555556`
- `brier`: `0.24116966760269293`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.24241986303102403`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0024302400027712188`
- `max_f1`: `0.9508196721311475`
- `model_storage_mb`: `0.4018745422363281`
- `nll`: `0.7739886610347682`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_pca16_mvtec_toothbrush_k4_seed4_calib_subspace_head_k4_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
