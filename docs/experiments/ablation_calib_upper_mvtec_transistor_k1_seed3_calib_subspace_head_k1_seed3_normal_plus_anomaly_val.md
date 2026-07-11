# Run ablation_calib_upper_mvtec_transistor_k1_seed3_calib_subspace_head_k1_seed3_normal_plus_anomaly_val

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_calib_upper_mvtec_transistor_k1_seed3.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.781859455870169`
- `auroc`: `0.8300925925925926`
- `brier`: `0.40828673052674214`
- `calibration_anomaly_val_count`: `4`
- `ece`: `0.4665180606146654`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0014358458768886824`
- `max_f1`: `0.7111111111111111`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `1.4704019557485124`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_calib_upper_mvtec_transistor_k1_seed3_calib_subspace_head_k1_seed3_normal_plus_anomaly_val/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
