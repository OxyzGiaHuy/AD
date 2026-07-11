# Run ablation_pca128_mvtec_capsule_k4_seed4_calib_subspace_head_k4_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca128_mvtec_capsule_k4_seed4.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9761720199585403`
- `auroc`: `0.901076984443558`
- `brier`: `0.13328328375403986`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.14154932241548185`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0022524812710330343`
- `max_f1`: `0.9357798165137615`
- `model_storage_mb`: `0.5659370422363281`
- `nll`: `0.6165370368485574`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_pca128_mvtec_capsule_k4_seed4_calib_subspace_head_k4_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
