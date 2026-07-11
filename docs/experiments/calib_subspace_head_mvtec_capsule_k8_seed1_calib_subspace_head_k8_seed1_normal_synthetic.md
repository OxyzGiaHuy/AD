# Run calib_subspace_head_mvtec_capsule_k8_seed1_calib_subspace_head_k8_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/calib_subspace_head_mvtec_capsule_k8_seed1.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9837893389543083`
- `auroc`: `0.9242122058236937`
- `brier`: `0.11911779190530651`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.12970124283861936`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0012730572542006319`
- `max_f1`: `0.9427312775330396`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `0.5393676201923427`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/calib_subspace_head_mvtec_capsule_k8_seed1_calib_subspace_head_k8_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
