# Run patchcore_mvtec_screw_k8_seed3_patchcore_k8_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/patchcore_mvtec_screw_k8_seed3.yaml`
- Dataset: `mvtec`
- Model: `patchcore`

## Metrics

- `ap`: `0.8873278908696132`
- `auroc`: `0.8112318097970895`
- `brier`: `0.7288017175734425`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.732119099481497`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.012343367980793118`
- `max_f1`: `0.8987854251012146`
- `model_storage_mb`: `6.0`
- `nll`: `3.463785806028003`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/patchcore_mvtec_screw_k8_seed3_patchcore_k8_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
