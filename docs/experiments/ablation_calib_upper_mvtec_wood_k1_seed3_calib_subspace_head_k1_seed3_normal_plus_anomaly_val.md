# Run ablation_calib_upper_mvtec_wood_k1_seed3_calib_subspace_head_k1_seed3_normal_plus_anomaly_val

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_calib_upper_mvtec_wood_k1_seed3.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9864074390673934`
- `auroc`: `0.9649122807017544`
- `brier`: `0.1613610894243853`
- `calibration_anomaly_val_count`: `6`
- `ece`: `0.18983393540121102`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.002401086106284024`
- `max_f1`: `0.9629629629629629`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `0.5462025753941779`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_calib_upper_mvtec_wood_k1_seed3_calib_subspace_head_k1_seed3_normal_plus_anomaly_val/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
