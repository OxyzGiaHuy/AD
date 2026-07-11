# Run ablation_pca32_mvtec_bottle_k8_seed2_calib_subspace_head_k8_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca32_mvtec_bottle_k8_seed2.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9818723627592091`
- `auroc`: `0.957936507936508`
- `brier`: `0.08411393716252025`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.11516106569668255`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.00207224239157625`
- `max_f1`: `0.96875`
- `model_storage_mb`: `0.4253120422363281`
- `nll`: `0.3693719279896346`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_pca32_mvtec_bottle_k8_seed2_calib_subspace_head_k8_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
