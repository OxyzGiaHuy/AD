# Run ablation_calib_upper_mvtec_hazelnut_k8_seed3_calib_subspace_head_k8_seed3_normal_plus_anomaly_val

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_calib_upper_mvtec_hazelnut_k8_seed3.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9903967667452345`
- `auroc`: `0.986904761904762`
- `brier`: `0.05121217939666007`
- `calibration_anomaly_val_count`: `7`
- `ece`: `0.1019150590867672`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.002092387020877264`
- `max_f1`: `0.976`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `0.2012751829943706`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_calib_upper_mvtec_hazelnut_k8_seed3_calib_subspace_head_k8_seed3_normal_plus_anomaly_val/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
