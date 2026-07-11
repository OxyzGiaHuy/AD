# Run ablation_calib_upper_mvtec_transistor_k4_seed2_calib_subspace_head_k4_seed2_normal_plus_anomaly_val

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_calib_upper_mvtec_transistor_k4_seed2.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.8397963536312937`
- `auroc`: `0.8828703703703704`
- `brier`: `0.19459726499638216`
- `calibration_anomaly_val_count`: `4`
- `ece`: `0.22488966727784523`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.002019523332516352`
- `max_f1`: `0.7619047619047619`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `0.7610360245566302`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_calib_upper_mvtec_transistor_k4_seed2_calib_subspace_head_k4_seed2_normal_plus_anomaly_val/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
