# Run patchcore_visa_pcb1_k8_seed3_patchcore_k8_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/visa_full/patchcore_visa_pcb1_k8_seed3.yaml`
- Dataset: `visa`
- Model: `patchcore`

## Metrics

- `ap`: `0.7429840397553684`
- `auroc`: `0.7864`
- `brier`: `0.4670149990310513`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.4614128929935396`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.11994532098993659`
- `max_f1`: `0.7699115044247787`
- `model_storage_mb`: `6.0`
- `nll`: `1.7144252958839972`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/patchcore_visa_pcb1_k8_seed3_patchcore_k8_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
