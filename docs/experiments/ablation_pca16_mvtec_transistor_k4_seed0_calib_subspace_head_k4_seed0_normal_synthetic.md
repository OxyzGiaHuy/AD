# Run ablation_pca16_mvtec_transistor_k4_seed0_calib_subspace_head_k4_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca16_mvtec_transistor_k4_seed0.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.7042879865189199`
- `auroc`: `0.7575`
- `brier`: `0.20543514130352894`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.1349253461137414`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.002047739941626787`
- `max_f1`: `0.6666666666666666`
- `model_storage_mb`: `0.4018745422363281`
- `nll`: `0.6319067975845204`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_pca16_mvtec_transistor_k4_seed0_calib_subspace_head_k4_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
