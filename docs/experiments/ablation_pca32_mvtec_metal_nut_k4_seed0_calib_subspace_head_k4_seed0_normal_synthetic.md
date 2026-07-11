# Run ablation_pca32_mvtec_metal_nut_k4_seed0_calib_subspace_head_k4_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca32_mvtec_metal_nut_k4_seed0.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9652793864990306`
- `auroc`: `0.8817204301075269`
- `brier`: `0.11800958781364844`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.13612660817478014`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0022120963296164637`
- `max_f1`: `0.9435897435897436`
- `model_storage_mb`: `0.4253120422363281`
- `nll`: `0.6336622327333319`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_pca32_mvtec_metal_nut_k4_seed0_calib_subspace_head_k4_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
