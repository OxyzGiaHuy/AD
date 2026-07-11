# Run ablation_pca128_mvtec_grid_k1_seed0_calib_subspace_head_k1_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca128_mvtec_grid_k1_seed0.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9747490785179003`
- `auroc`: `0.9406850459482038`
- `brier`: `0.26892863210794754`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.26907899058782137`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0025205955100365174`
- `max_f1`: `0.95`
- `model_storage_mb`: `0.5659370422363281`
- `nll`: `3.2684141128892126`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_pca128_mvtec_grid_k1_seed0_calib_subspace_head_k1_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
