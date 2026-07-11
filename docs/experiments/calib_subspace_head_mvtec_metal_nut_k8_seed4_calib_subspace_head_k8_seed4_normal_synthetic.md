# Run calib_subspace_head_mvtec_metal_nut_k8_seed4_calib_subspace_head_k8_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/calib_subspace_head_mvtec_metal_nut_k8_seed4.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9818534890482227`
- `auroc`: `0.9354838709677419`
- `brier`: `0.10367285370072593`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.12193695274384123`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.001280528468930203`
- `max_f1`: `0.9528795811518325`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `0.46993352345195527`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/calib_subspace_head_mvtec_metal_nut_k8_seed4_calib_subspace_head_k8_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
