# Run ablation_calib_upper_mvtec_pill_k8_seed4_calib_subspace_head_k8_seed4_normal_plus_anomaly_val

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_calib_upper_mvtec_pill_k8_seed4.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9853490631358003`
- `auroc`: `0.9412477286493035`
- `brier`: `0.06379363329908312`
- `calibration_anomaly_val_count`: `14`
- `ece`: `0.0691414237885243`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.002663803889470942`
- `max_f1`: `0.9561752988047809`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `0.22021639036958515`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_calib_upper_mvtec_pill_k8_seed4_calib_subspace_head_k8_seed4_normal_plus_anomaly_val/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
