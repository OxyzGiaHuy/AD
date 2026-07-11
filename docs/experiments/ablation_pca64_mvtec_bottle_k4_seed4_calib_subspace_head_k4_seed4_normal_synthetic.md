# Run ablation_pca64_mvtec_bottle_k4_seed4_calib_subspace_head_k4_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca64_mvtec_bottle_k4_seed4.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9972574269676489`
- `auroc`: `0.9912698412698413`
- `brier`: `0.15634931703350677`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.17957492729267444`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0017543090844010733`
- `max_f1`: `0.9841269841269841`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `0.7986775491271219`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_pca64_mvtec_bottle_k4_seed4_calib_subspace_head_k4_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
