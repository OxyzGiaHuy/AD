# Run anomalydino_visa_pcb3_k8_seed0_anomalydino_k8_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/visa_full/anomalydino_visa_pcb3_k8_seed0.yaml`
- Dataset: `visa`
- Model: `anomalydino`

## Metrics

- `ap`: `0.7808853447183094`
- `auroc`: `0.7996039603960396`
- `brier`: `0.47265791985281713`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.467771507452117`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.09279189875988818`
- `max_f1`: `0.7622950819672131`
- `model_storage_mb`: `6.0`
- `nll`: `1.846192827278618`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/anomalydino_visa_pcb3_k8_seed0_anomalydino_k8_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
