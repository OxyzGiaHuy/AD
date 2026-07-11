# Run ablation_calib_upper_mvtec_wood_k8_seed4_calib_subspace_head_k8_seed4_normal_plus_anomaly_val

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_calib_upper_mvtec_wood_k8_seed4.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9895888860945542`
- `auroc`: `0.9746588693957114`
- `brier`: `0.1033284984109652`
- `calibration_anomaly_val_count`: `6`
- `ece`: `0.13772547622657808`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.004043909861412767`
- `max_f1`: `0.9724770642201835`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `0.37934657555926016`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_calib_upper_mvtec_wood_k8_seed4_calib_subspace_head_k8_seed4_normal_plus_anomaly_val/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
