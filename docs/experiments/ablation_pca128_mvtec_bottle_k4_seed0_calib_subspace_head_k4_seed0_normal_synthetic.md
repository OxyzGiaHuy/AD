# Run ablation_pca128_mvtec_bottle_k4_seed0_calib_subspace_head_k4_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca128_mvtec_bottle_k4_seed0.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9995000314940792`
- `auroc`: `0.9984126984126984`
- `brier`: `0.1887880430248606`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.20807815028960439`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0034937090408730218`
- `max_f1`: `0.9921259842519685`
- `model_storage_mb`: `0.5659370422363281`
- `nll`: `0.7355407770215165`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_pca128_mvtec_bottle_k4_seed0_calib_subspace_head_k4_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
