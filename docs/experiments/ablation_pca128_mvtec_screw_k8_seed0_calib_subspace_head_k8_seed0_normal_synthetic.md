# Run ablation_pca128_mvtec_screw_k8_seed0_calib_subspace_head_k8_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca128_mvtec_screw_k8_seed0.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.898064483050088`
- `auroc`: `0.8233244517319123`
- `brier`: `0.13830541105366478`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.12206526085210498`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0029268032521940768`
- `max_f1`: `0.9133858267716536`
- `model_storage_mb`: `0.5659370422363281`
- `nll`: `0.5442501824623835`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_pca128_mvtec_screw_k8_seed0_calib_subspace_head_k8_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
