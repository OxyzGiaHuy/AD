# Run patchcore_visa_pipe_fryum_k8_seed0_patchcore_k8_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/visa_full/patchcore_visa_pipe_fryum_k8_seed0.yaml`
- Dataset: `visa`
- Model: `patchcore`

## Metrics

- `ap`: `0.9909291164024662`
- `auroc`: `0.9814`
- `brier`: `0.6617325094488642`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.659869131197532`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.07412919363627832`
- `max_f1`: `0.9556650246305419`
- `model_storage_mb`: `6.0`
- `nll`: `3.7887216053449833`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/patchcore_visa_pipe_fryum_k8_seed0_patchcore_k8_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
