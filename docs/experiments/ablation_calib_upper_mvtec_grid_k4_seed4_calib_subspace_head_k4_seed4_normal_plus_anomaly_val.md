# Run ablation_calib_upper_mvtec_grid_k4_seed4_calib_subspace_head_k4_seed4_normal_plus_anomaly_val

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_calib_upper_mvtec_grid_k4_seed4.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9985812264658419`
- `auroc`: `0.9963369963369964`
- `brier`: `0.03943702029845383`
- `calibration_anomaly_val_count`: `5`
- `ece`: `0.07568313280911475`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0031663918842191564`
- `max_f1`: `0.9807692307692307`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `0.1333317952874807`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_calib_upper_mvtec_grid_k4_seed4_calib_subspace_head_k4_seed4_normal_plus_anomaly_val/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
