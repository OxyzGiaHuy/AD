# Run ablation_calib_upper_mvtec_cable_k8_seed4_calib_subspace_head_k8_seed4_normal_plus_anomaly_val

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_calib_upper_mvtec_cable_k8_seed4.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9532415609837935`
- `auroc`: `0.9094308267552971`
- `brier`: `0.22280993002152896`
- `calibration_anomaly_val_count`: `9`
- `ece`: `0.2590227505416735`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.001479482833058276`
- `max_f1`: `0.9019607843137255`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `0.5856511599977912`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_calib_upper_mvtec_cable_k8_seed4_calib_subspace_head_k8_seed4_normal_plus_anomaly_val/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
