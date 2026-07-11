# Run ablation_pca32_mvtec_leather_k4_seed1_calib_subspace_head_k4_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca32_mvtec_leather_k4_seed1.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9973227398665191`
- `auroc`: `0.9921875`
- `brier`: `0.2069658540126269`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.20097510035960903`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0016472138794920137`
- `max_f1`: `0.9732620320855615`
- `model_storage_mb`: `0.4253120422363281`
- `nll`: `0.647188572756389`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_pca32_mvtec_leather_k4_seed1_calib_subspace_head_k4_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
