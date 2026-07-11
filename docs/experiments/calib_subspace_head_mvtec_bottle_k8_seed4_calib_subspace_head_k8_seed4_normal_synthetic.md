# Run calib_subspace_head_mvtec_bottle_k8_seed4_calib_subspace_head_k8_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/calib_subspace_head_mvtec_bottle_k8_seed4.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9967916942976308`
- `auroc`: `0.9904761904761905`
- `brier`: `0.12696767677471205`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.14571978655890624`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0012790950082511787`
- `max_f1`: `0.984375`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `0.6555425608580354`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/calib_subspace_head_mvtec_bottle_k8_seed4_calib_subspace_head_k8_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
