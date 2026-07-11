# Run ablation_pca128_mvtec_hazelnut_k8_seed2_calib_subspace_head_k8_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca128_mvtec_hazelnut_k8_seed2.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9979939178257534`
- `auroc`: `0.9964285714285714`
- `brier`: `0.2058035539425492`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.24870725045488645`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.013217387991872701`
- `max_f1`: `0.9787234042553191`
- `model_storage_mb`: `0.5659370422363281`
- `nll`: `0.7623800563221794`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_pca128_mvtec_hazelnut_k8_seed2_calib_subspace_head_k8_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
