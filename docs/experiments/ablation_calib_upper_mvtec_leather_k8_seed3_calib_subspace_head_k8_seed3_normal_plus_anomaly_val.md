# Run ablation_calib_upper_mvtec_leather_k8_seed3_calib_subspace_head_k8_seed3_normal_plus_anomaly_val

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_calib_upper_mvtec_leather_k8_seed3.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `1.0`
- `auroc`: `1.0`
- `brier`: `0.0030788201122381297`
- `calibration_anomaly_val_count`: `9`
- `ece`: `0.02534939042980906`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0023677884884502577`
- `max_f1`: `1.0`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `0.02722613034184204`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_calib_upper_mvtec_leather_k8_seed3_calib_subspace_head_k8_seed3_normal_plus_anomaly_val/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
