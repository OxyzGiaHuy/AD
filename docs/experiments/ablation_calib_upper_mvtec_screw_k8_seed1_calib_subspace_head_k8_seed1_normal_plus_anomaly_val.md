# Run ablation_calib_upper_mvtec_screw_k8_seed1_calib_subspace_head_k8_seed1_normal_plus_anomaly_val

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_calib_upper_mvtec_screw_k8_seed1.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.8994872223944668`
- `auroc`: `0.8048780487804879`
- `brier`: `0.20454038299684682`
- `calibration_anomaly_val_count`: `11`
- `ece`: `0.19439227809041937`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.001473290333211822`
- `max_f1`: `0.8717948717948718`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `0.6817959813541278`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_calib_upper_mvtec_screw_k8_seed1_calib_subspace_head_k8_seed1_normal_plus_anomaly_val/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
