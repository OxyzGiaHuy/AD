# Run anomalydino_visa_pcb4_k4_seed2_anomalydino_k4_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/visa_full/anomalydino_visa_pcb4_k4_seed2.yaml`
- Dataset: `visa`
- Model: `anomalydino`

## Metrics

- `ap`: `0.7412702553385186`
- `auroc`: `0.7903960396039604`
- `brier`: `0.4762310804614122`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.472447052987209`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.07587850369068223`
- `max_f1`: `0.7609756097560976`
- `model_storage_mb`: `6.0`
- `nll`: `1.9216879493149228`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/anomalydino_visa_pcb4_k4_seed2_anomalydino_k4_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
