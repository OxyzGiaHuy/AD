# Run ablation_calib_upper_mvtec_capsule_k4_seed4_calib_subspace_head_k4_seed4_normal_plus_anomaly_val

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_calib_upper_mvtec_capsule_k4_seed4.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9636911183566892`
- `auroc`: `0.8708827404479579`
- `brier`: `0.132907345191208`
- `calibration_anomaly_val_count`: `10`
- `ece`: `0.12501477755484036`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.002366752989712309`
- `max_f1`: `0.9313725490196079`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `0.45272053097832915`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_calib_upper_mvtec_capsule_k4_seed4_calib_subspace_head_k4_seed4_normal_plus_anomaly_val/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
