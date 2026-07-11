# Run patchcore_mvtec_zipper_k8_seed1_patchcore_k8_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/patchcore_mvtec_zipper_k8_seed1.yaml`
- Dataset: `mvtec`
- Model: `patchcore`

## Metrics

- `ap`: `0.9933426954653631`
- `auroc`: `0.9787289915966386`
- `brier`: `0.7668066664345887`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.7696068373644441`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.012453786115970044`
- `max_f1`: `0.979253112033195`
- `model_storage_mb`: `6.0`
- `nll`: `3.467008971083234`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/patchcore_mvtec_zipper_k8_seed1_patchcore_k8_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
