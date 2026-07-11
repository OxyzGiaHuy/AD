# Run ablation_calib_upper_mvtec_wood_k8_seed3_calib_subspace_head_k8_seed3_normal_plus_anomaly_val

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_calib_upper_mvtec_wood_k8_seed3.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9830450547079445`
- `auroc`: `0.9600389863547758`
- `brier`: `0.07584293352395557`
- `calibration_anomaly_val_count`: `6`
- `ece`: `0.100163247602137`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0018599533463177615`
- `max_f1`: `0.9724770642201835`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `0.2970558837619697`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_calib_upper_mvtec_wood_k8_seed3_calib_subspace_head_k8_seed3_normal_plus_anomaly_val/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
