# Run anomalydino_visa_pcb2_k4_seed1_anomalydino_k4_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/visa_full/anomalydino_visa_pcb2_k4_seed1.yaml`
- Dataset: `visa`
- Model: `anomalydino`

## Metrics

- `ap`: `0.636075517649098`
- `auroc`: `0.6845`
- `brier`: `0.4880434817158788`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.4861991889681667`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.12428845717571675`
- `max_f1`: `0.7258687258687259`
- `model_storage_mb`: `6.0`
- `nll`: `2.2428861409487357`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/anomalydino_visa_pcb2_k4_seed1_anomalydino_k4_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
