# Run ablation_pca128_mvtec_tile_k8_seed1_calib_subspace_head_k8_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca128_mvtec_tile_k8_seed1.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9928980264097504`
- `auroc`: `0.9834054834054834`
- `brier`: `0.06948795988969128`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.09585189762819782`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0018626787723639072`
- `max_f1`: `0.9767441860465116`
- `model_storage_mb`: `0.5659370422363281`
- `nll`: `0.29608665852369453`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_pca128_mvtec_tile_k8_seed1_calib_subspace_head_k8_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
