# Run ablation_calib_upper_mvtec_toothbrush_k1_seed3_calib_subspace_head_k1_seed3_normal_plus_anomaly_val

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_calib_upper_mvtec_toothbrush_k1_seed3.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.979735335519137`
- `auroc`: `0.9537037037037037`
- `brier`: `0.12890220670793615`
- `calibration_anomaly_val_count`: `3`
- `ece`: `0.15577527431723398`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.004167538422804613`
- `max_f1`: `0.9310344827586207`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `0.41208874266582385`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_calib_upper_mvtec_toothbrush_k1_seed3_calib_subspace_head_k1_seed3_normal_plus_anomaly_val/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
