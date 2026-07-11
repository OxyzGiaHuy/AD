# Run calib_subspace_head_mvtec_zipper_k8_seed1_calib_subspace_head_k8_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/calib_subspace_head_mvtec_zipper_k8_seed1.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9860114712943848`
- `auroc`: `0.9495798319327731`
- `brier`: `0.11368017859605206`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.13196487611295366`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.00132208802299389`
- `max_f1`: `0.9477911646586346`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `0.43999984731778086`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/calib_subspace_head_mvtec_zipper_k8_seed1_calib_subspace_head_k8_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
