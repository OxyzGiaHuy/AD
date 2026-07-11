# Run ablation_calib_upper_mvtec_carpet_k1_seed3_calib_subspace_head_k1_seed3_normal_plus_anomaly_val

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_calib_upper_mvtec_carpet_k1_seed3.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9984934695960391`
- `auroc`: `0.9955908289241623`
- `brier`: `0.024918883234708113`
- `calibration_anomaly_val_count`: `8`
- `ece`: `0.05167316860698783`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0016279253561835771`
- `max_f1`: `0.9818181818181818`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `0.09947320026004466`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_calib_upper_mvtec_carpet_k1_seed3_calib_subspace_head_k1_seed3_normal_plus_anomaly_val/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
