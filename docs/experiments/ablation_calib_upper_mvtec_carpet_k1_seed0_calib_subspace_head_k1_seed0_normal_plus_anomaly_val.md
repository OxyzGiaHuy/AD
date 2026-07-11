# Run ablation_calib_upper_mvtec_carpet_k1_seed0_calib_subspace_head_k1_seed0_normal_plus_anomaly_val

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_calib_upper_mvtec_carpet_k1_seed0.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9956534293632245`
- `auroc`: `0.9876543209876543`
- `brier`: `0.045861862501763904`
- `calibration_anomaly_val_count`: `8`
- `ece`: `0.07825420455101433`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0015907725746478509`
- `max_f1`: `0.9818181818181818`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `0.1731391085745`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_calib_upper_mvtec_carpet_k1_seed0_calib_subspace_head_k1_seed0_normal_plus_anomaly_val/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
