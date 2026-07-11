# Run ablation_calib_upper_mvtec_toothbrush_k4_seed2_calib_subspace_head_k4_seed2_normal_plus_anomaly_val

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_calib_upper_mvtec_toothbrush_k4_seed2.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9846344629430864`
- `auroc`: `0.9660493827160493`
- `brier`: `0.06273824242408896`
- `calibration_anomaly_val_count`: `3`
- `ece`: `0.11240221235232473`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.004308290301989286`
- `max_f1`: `0.9642857142857143`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `0.22877970513106782`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_calib_upper_mvtec_toothbrush_k4_seed2_calib_subspace_head_k4_seed2_normal_plus_anomaly_val/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
