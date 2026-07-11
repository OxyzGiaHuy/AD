# Run ablation_pca32_mvtec_bottle_k4_seed2_calib_subspace_head_k4_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca32_mvtec_bottle_k4_seed2.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9859075424136257`
- `auroc`: `0.9642857142857143`
- `brier`: `0.08894698197826345`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.10758420618542705`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0031140652002699405`
- `max_f1`: `0.9692307692307692`
- `model_storage_mb`: `0.4253120422363281`
- `nll`: `0.40324883484132495`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_pca32_mvtec_bottle_k4_seed2_calib_subspace_head_k4_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
