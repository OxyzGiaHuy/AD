# Run ablation_pca64_mvtec_wood_k1_seed2_calib_subspace_head_k1_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca64_mvtec_wood_k1_seed2.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9888443791181537`
- `auroc`: `0.9631578947368421`
- `brier`: `0.2404853254487262`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.2404957979540281`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.002760911879094341`
- `max_f1`: `0.9572649572649573`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `3.3103233820844378`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_pca64_mvtec_wood_k1_seed2_calib_subspace_head_k1_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
