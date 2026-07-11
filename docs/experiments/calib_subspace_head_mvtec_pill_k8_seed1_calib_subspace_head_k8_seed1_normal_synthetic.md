# Run calib_subspace_head_mvtec_pill_k8_seed1_calib_subspace_head_k8_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/calib_subspace_head_mvtec_pill_k8_seed1.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9886647404758329`
- `auroc`: `0.9489907255864702`
- `brier`: `0.0670487157813939`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.07501454868710813`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.001312689799926952`
- `max_f1`: `0.9616724738675958`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `0.32389275756155483`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/calib_subspace_head_mvtec_pill_k8_seed1_calib_subspace_head_k8_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
