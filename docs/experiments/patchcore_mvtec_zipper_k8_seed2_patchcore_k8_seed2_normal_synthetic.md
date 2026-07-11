# Run patchcore_mvtec_zipper_k8_seed2_patchcore_k8_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/patchcore_mvtec_zipper_k8_seed2.yaml`
- Dataset: `mvtec`
- Model: `patchcore`

## Metrics

- `ap`: `0.9949530519846995`
- `auroc`: `0.9829306722689075`
- `brier`: `0.7420382067287424`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.7569631224140427`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.012583559835391328`
- `max_f1`: `0.9752066115702479`
- `model_storage_mb`: `6.0`
- `nll`: `2.7985240031977314`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/patchcore_mvtec_zipper_k8_seed2_patchcore_k8_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
