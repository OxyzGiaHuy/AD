# Run patchcore_visa_fryum_k8_seed1_patchcore_k8_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/visa_full/patchcore_visa_fryum_k8_seed1.yaml`
- Dataset: `visa`
- Model: `patchcore`

## Metrics

- `ap`: `0.9813998633570331`
- `auroc`: `0.9602`
- `brier`: `0.5792189754909746`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.5896011130511761`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.07712864433725675`
- `max_f1`: `0.9292929292929293`
- `model_storage_mb`: `6.0`
- `nll`: `1.8083099453943408`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/patchcore_visa_fryum_k8_seed1_patchcore_k8_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
