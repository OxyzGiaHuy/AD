# Run ablation_calib_upper_mvtec_transistor_k8_seed2_calib_subspace_head_k8_seed2_normal_plus_anomaly_val

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_calib_upper_mvtec_transistor_k8_seed2.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.8401498322373379`
- `auroc`: `0.8805555555555555`
- `brier`: `0.17679437947475118`
- `calibration_anomaly_val_count`: `4`
- `ece`: `0.16759313772884826`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.00230312409500281`
- `max_f1`: `0.7605633802816901`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `0.6140339654778649`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_calib_upper_mvtec_transistor_k8_seed2_calib_subspace_head_k8_seed2_normal_plus_anomaly_val/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
