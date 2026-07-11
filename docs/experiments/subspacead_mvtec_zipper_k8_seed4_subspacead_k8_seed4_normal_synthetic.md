# Run subspacead_mvtec_zipper_k8_seed4_subspacead_k8_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/subspacead_mvtec_zipper_k8_seed4.yaml`
- Dataset: `mvtec`
- Model: `subspacead`

## Metrics

- `ap`: `0.9931848610070828`
- `auroc`: `0.9753151260504201`
- `brier`: `0.36697594099957365`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.5052319759169951`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.001276921345204707`
- `max_f1`: `0.9554655870445344`
- `model_storage_mb`: `0.09521484375`
- `nll`: `0.9387308578655533`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/subspacead_mvtec_zipper_k8_seed4_subspacead_k8_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
