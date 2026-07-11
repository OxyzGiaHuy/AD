# Run ablation_pca32_mvtec_transistor_k8_seed1_calib_subspace_head_k8_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca32_mvtec_transistor_k8_seed1.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.8458225783420001`
- `auroc`: `0.8720833333333333`
- `brier`: `0.1706770497657427`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.15898425474297256`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0023265396431088447`
- `max_f1`: `0.75`
- `model_storage_mb`: `0.4253120422363281`
- `nll`: `0.5728146458354295`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_pca32_mvtec_transistor_k8_seed1_calib_subspace_head_k8_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
