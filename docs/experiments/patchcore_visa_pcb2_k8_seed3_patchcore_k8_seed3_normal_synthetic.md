# Run patchcore_visa_pcb2_k8_seed3_patchcore_k8_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/visa_full/patchcore_visa_pcb2_k8_seed3.yaml`
- Dataset: `visa`
- Model: `patchcore`

## Metrics

- `ap`: `0.6930161180814204`
- `auroc`: `0.7343`
- `brier`: `0.48854536792769304`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.48669696422526615`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.10380684060044587`
- `max_f1`: `0.728744939271255`
- `model_storage_mb`: `6.0`
- `nll`: `2.259603916046075`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/patchcore_visa_pcb2_k8_seed3_patchcore_k8_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
