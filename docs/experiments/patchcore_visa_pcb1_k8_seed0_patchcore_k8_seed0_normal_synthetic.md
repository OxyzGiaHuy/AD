# Run patchcore_visa_pcb1_k8_seed0_patchcore_k8_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/visa_full/patchcore_visa_pcb1_k8_seed0.yaml`
- Dataset: `visa`
- Model: `patchcore`

## Metrics

- `ap`: `0.8688607146752301`
- `auroc`: `0.8882`
- `brier`: `0.4924257217421049`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.4888984835264273`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0629544670227915`
- `max_f1`: `0.827906976744186`
- `model_storage_mb`: `6.0`
- `nll`: `2.4665701579191044`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/patchcore_visa_pcb1_k8_seed0_patchcore_k8_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
