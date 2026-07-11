# Run ablation_pca16_mvtec_tile_k1_seed4_calib_subspace_head_k1_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca16_mvtec_tile_k1_seed4.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9906269310592218`
- `auroc`: `0.9772727272727273`
- `brier`: `0.24051995502584086`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.22477525720993674`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.002263188823802858`
- `max_f1`: `0.9655172413793104`
- `model_storage_mb`: `0.4018745422363281`
- `nll`: `0.7820798891215013`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_pca16_mvtec_tile_k1_seed4_calib_subspace_head_k1_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
