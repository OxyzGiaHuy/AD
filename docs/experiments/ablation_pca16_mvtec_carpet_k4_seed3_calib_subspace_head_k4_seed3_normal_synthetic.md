# Run ablation_pca16_mvtec_carpet_k4_seed3_calib_subspace_head_k4_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca16_mvtec_carpet_k4_seed3.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9963841732306322`
- `auroc`: `0.9879614767255217`
- `brier`: `0.25740125957680277`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.25101215863584453`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.002418784376902458`
- `max_f1`: `0.9777777777777777`
- `model_storage_mb`: `0.4018745422363281`
- `nll`: `0.7673928651622821`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_pca16_mvtec_carpet_k4_seed3_calib_subspace_head_k4_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
