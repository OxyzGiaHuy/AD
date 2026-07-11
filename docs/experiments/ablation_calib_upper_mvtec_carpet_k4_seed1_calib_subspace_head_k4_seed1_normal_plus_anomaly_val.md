# Run ablation_calib_upper_mvtec_carpet_k4_seed1_calib_subspace_head_k4_seed1_normal_plus_anomaly_val

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_calib_upper_mvtec_carpet_k4_seed1.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.996939140100412`
- `auroc`: `0.9911816578483245`
- `brier`: `0.030396728450754855`
- `calibration_anomaly_val_count`: `8`
- `ece`: `0.0520934846611061`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.00302714254672921`
- `max_f1`: `0.9818181818181818`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `0.10846401085911354`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_calib_upper_mvtec_carpet_k4_seed1_calib_subspace_head_k4_seed1_normal_plus_anomaly_val/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
