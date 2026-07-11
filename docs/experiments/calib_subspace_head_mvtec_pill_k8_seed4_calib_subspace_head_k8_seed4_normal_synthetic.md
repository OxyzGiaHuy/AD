# Run calib_subspace_head_mvtec_pill_k8_seed4_calib_subspace_head_k8_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/calib_subspace_head_mvtec_pill_k8_seed4.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9870421261278943`
- `auroc`: `0.9429896344789962`
- `brier`: `0.06053877080891853`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.07516459454322223`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0012799548821713397`
- `max_f1`: `0.9605734767025089`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `0.23934561029275392`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/calib_subspace_head_mvtec_pill_k8_seed4_calib_subspace_head_k8_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
