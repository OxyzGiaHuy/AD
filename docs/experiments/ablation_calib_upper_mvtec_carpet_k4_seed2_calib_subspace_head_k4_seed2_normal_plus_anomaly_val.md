# Run ablation_calib_upper_mvtec_carpet_k4_seed2_calib_subspace_head_k4_seed2_normal_plus_anomaly_val

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_calib_upper_mvtec_carpet_k4_seed2.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9988080219499724`
- `auroc`: `0.9964726631393298`
- `brier`: `0.024224469932795527`
- `calibration_anomaly_val_count`: `8`
- `ece`: `0.05000055391649042`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0024882426331622885`
- `max_f1`: `0.9818181818181818`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `0.0884235527277097`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_calib_upper_mvtec_carpet_k4_seed2_calib_subspace_head_k4_seed2_normal_plus_anomaly_val/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
