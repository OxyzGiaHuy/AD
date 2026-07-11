# Run ablation_calib_upper_mvtec_cable_k4_seed0_calib_subspace_head_k4_seed0_normal_plus_anomaly_val

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_calib_upper_mvtec_cable_k4_seed0.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9487507200176085`
- `auroc`: `0.9090153718321562`
- `brier`: `0.3026486664361287`
- `calibration_anomaly_val_count`: `9`
- `ece`: `0.32815203260868153`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0023256655623938175`
- `max_f1`: `0.8888888888888888`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `0.9105647041321595`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_calib_upper_mvtec_cable_k4_seed0_calib_subspace_head_k4_seed0_normal_plus_anomaly_val/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
