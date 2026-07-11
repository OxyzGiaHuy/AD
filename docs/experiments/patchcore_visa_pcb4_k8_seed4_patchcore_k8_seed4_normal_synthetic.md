# Run patchcore_visa_pcb4_k8_seed4_patchcore_k8_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/visa_full/patchcore_visa_pcb4_k8_seed4.yaml`
- Dataset: `visa`
- Model: `patchcore`

## Metrics

- `ap`: `0.8380279290100968`
- `auroc`: `0.8817821782178218`
- `brier`: `0.4800541468269372`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.47400001726988983`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.07659242917500918`
- `max_f1`: `0.8546255506607929`
- `model_storage_mb`: `6.0`
- `nll`: `2.0174657719468505`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/patchcore_visa_pcb4_k8_seed4_patchcore_k8_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
