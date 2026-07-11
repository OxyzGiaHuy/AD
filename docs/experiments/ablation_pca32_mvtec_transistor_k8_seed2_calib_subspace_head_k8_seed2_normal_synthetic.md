# Run ablation_pca32_mvtec_transistor_k8_seed2_calib_subspace_head_k8_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca32_mvtec_transistor_k8_seed2.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.7827513837698353`
- `auroc`: `0.8275`
- `brier`: `0.23163508712226943`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.2880324322171509`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0022913413494825364`
- `max_f1`: `0.7021276595744681`
- `model_storage_mb`: `0.4253120422363281`
- `nll`: `0.7447106804021701`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_pca32_mvtec_transistor_k8_seed2_calib_subspace_head_k8_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
