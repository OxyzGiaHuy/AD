# Run ablation_calib_upper_mvtec_tile_k1_seed0_calib_subspace_head_k1_seed0_normal_plus_anomaly_val

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_calib_upper_mvtec_tile_k1_seed0.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9933275382065246`
- `auroc`: `0.9860446570972887`
- `brier`: `0.20960148083790575`
- `calibration_anomaly_val_count`: `8`
- `ece`: `0.2396505557068991`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0021453168619116514`
- `max_f1`: `0.9743589743589743`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `0.5854203511597684`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_calib_upper_mvtec_tile_k1_seed0_calib_subspace_head_k1_seed0_normal_plus_anomaly_val/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
