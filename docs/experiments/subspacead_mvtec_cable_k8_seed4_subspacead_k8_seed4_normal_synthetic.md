# Run subspacead_mvtec_cable_k8_seed4_subspacead_k8_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/subspacead_mvtec_cable_k8_seed4.yaml`
- Dataset: `mvtec`
- Model: `subspacead`

## Metrics

- `ap`: `0.9566936078738982`
- `auroc`: `0.9104197901049476`
- `brier`: `0.38614795893215054`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.3863336881001791`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0013585731262962023`
- `max_f1`: `0.8994082840236687`
- `model_storage_mb`: `0.09521484375`
- `nll`: `2.9313805616907347`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/subspacead_mvtec_cable_k8_seed4_subspacead_k8_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
