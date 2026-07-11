# Run ablation_calib_upper_mvtec_bottle_k8_seed0_calib_subspace_head_k8_seed0_normal_plus_anomaly_val

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_calib_upper_mvtec_bottle_k8_seed0.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9950017139835554`
- `auroc`: `0.9868421052631579`
- `brier`: `0.035327329842402506`
- `calibration_anomaly_val_count`: `6`
- `ece`: `0.05689124286465058`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.002385305869695428`
- `max_f1`: `0.9827586206896551`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `0.13983524243204634`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_calib_upper_mvtec_bottle_k8_seed0_calib_subspace_head_k8_seed0_normal_plus_anomaly_val/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
