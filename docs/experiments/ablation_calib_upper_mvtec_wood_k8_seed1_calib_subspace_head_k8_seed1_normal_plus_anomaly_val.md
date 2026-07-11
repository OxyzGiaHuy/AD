# Run ablation_calib_upper_mvtec_wood_k8_seed1_calib_subspace_head_k8_seed1_normal_plus_anomaly_val

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_calib_upper_mvtec_wood_k8_seed1.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9879544759355018`
- `auroc`: `0.9688109161793372`
- `brier`: `0.07894608951664575`
- `calibration_anomaly_val_count`: `6`
- `ece`: `0.09923549755540206`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0025200275831843075`
- `max_f1`: `0.9636363636363636`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `0.33424943075107894`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_calib_upper_mvtec_wood_k8_seed1_calib_subspace_head_k8_seed1_normal_plus_anomaly_val/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
