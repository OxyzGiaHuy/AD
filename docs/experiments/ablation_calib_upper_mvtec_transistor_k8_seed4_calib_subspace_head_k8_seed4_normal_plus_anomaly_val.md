# Run ablation_calib_upper_mvtec_transistor_k8_seed4_calib_subspace_head_k8_seed4_normal_plus_anomaly_val

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_calib_upper_mvtec_transistor_k8_seed4.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.8960721585269403`
- `auroc`: `0.9254629629629629`
- `brier`: `0.12140707788546325`
- `calibration_anomaly_val_count`: `4`
- `ece`: `0.17222551190449548`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0015797360489765804`
- `max_f1`: `0.8484848484848485`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `0.4000451248774575`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_calib_upper_mvtec_transistor_k8_seed4_calib_subspace_head_k8_seed4_normal_plus_anomaly_val/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
