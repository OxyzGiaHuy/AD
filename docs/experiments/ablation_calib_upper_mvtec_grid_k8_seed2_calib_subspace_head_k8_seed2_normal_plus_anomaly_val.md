# Run ablation_calib_upper_mvtec_grid_k8_seed2_calib_subspace_head_k8_seed2_normal_plus_anomaly_val

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_calib_upper_mvtec_grid_k8_seed2.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `1.0`
- `auroc`: `1.0`
- `brier`: `0.004520166918853336`
- `calibration_anomaly_val_count`: `5`
- `ece`: `0.03472592786260662`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.002208602601942951`
- `max_f1`: `1.0`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `0.03737009744589903`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_calib_upper_mvtec_grid_k8_seed2_calib_subspace_head_k8_seed2_normal_plus_anomaly_val/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
