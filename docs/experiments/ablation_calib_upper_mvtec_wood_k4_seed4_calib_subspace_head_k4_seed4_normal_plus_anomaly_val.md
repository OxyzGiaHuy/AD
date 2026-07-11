# Run ablation_calib_upper_mvtec_wood_k4_seed4_calib_subspace_head_k4_seed4_normal_plus_anomaly_val

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_calib_upper_mvtec_wood_k4_seed4.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9896236042468382`
- `auroc`: `0.9727095516569201`
- `brier`: `0.1359427482182049`
- `calibration_anomaly_val_count`: `6`
- `ece`: `0.1723358765856861`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.004377444797795112`
- `max_f1`: `0.9636363636363636`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `0.494770335312672`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_calib_upper_mvtec_wood_k4_seed4_calib_subspace_head_k4_seed4_normal_plus_anomaly_val/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
