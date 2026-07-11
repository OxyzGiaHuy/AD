# Run ablation_calib_upper_mvtec_wood_k4_seed0_calib_subspace_head_k4_seed0_normal_plus_anomaly_val

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_calib_upper_mvtec_wood_k4_seed0.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9762568583822768`
- `auroc`: `0.9395711500974658`
- `brier`: `0.10212269656920464`
- `calibration_anomaly_val_count`: `6`
- `ece`: `0.12634119825208023`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0019295605486386444`
- `max_f1`: `0.9310344827586207`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `0.375442910849014`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_calib_upper_mvtec_wood_k4_seed0_calib_subspace_head_k4_seed0_normal_plus_anomaly_val/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
