# Run patchcore_mvtec_pill_k8_seed2_patchcore_k8_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/patchcore_mvtec_pill_k8_seed2.yaml`
- Dataset: `mvtec`
- Model: `patchcore`

## Metrics

- `ap`: `0.9868055298579829`
- `auroc`: `0.9345335515548282`
- `brier`: `0.8331961770288058`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.8362068716306964`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.01204971128148947`
- `max_f1`: `0.9543859649122807`
- `model_storage_mb`: `6.0`
- `nll`: `4.335705412616144`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/patchcore_mvtec_pill_k8_seed2_patchcore_k8_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
