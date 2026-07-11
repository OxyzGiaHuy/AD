# Run patchcore_visa_capsules_k8_seed3_patchcore_k8_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/visa_full/patchcore_visa_capsules_k8_seed3.yaml`
- Dataset: `visa`
- Model: `patchcore`

## Metrics

- `ap`: `0.9356397563770011`
- `auroc`: `0.9145`
- `brier`: `0.6120920694153617`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.6101897072134307`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.07175201582722365`
- `max_f1`: `0.9004739336492891`
- `model_storage_mb`: `6.0`
- `nll`: `2.9134829727791693`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/patchcore_visa_capsules_k8_seed3_patchcore_k8_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
