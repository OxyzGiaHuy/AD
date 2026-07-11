# Run ablation_calib_upper_mvtec_transistor_k8_seed3_calib_subspace_head_k8_seed3_normal_plus_anomaly_val

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_calib_upper_mvtec_transistor_k8_seed3.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.7771398865538524`
- `auroc`: `0.8379629629629629`
- `brier`: `0.27654351828230134`
- `calibration_anomaly_val_count`: `4`
- `ece`: `0.3143274327643061`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0014298487027796607`
- `max_f1`: `0.717948717948718`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `1.1039929469219696`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_calib_upper_mvtec_transistor_k8_seed3_calib_subspace_head_k8_seed3_normal_plus_anomaly_val/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
