# Run ablation_pca32_mvtec_transistor_k8_seed3_calib_subspace_head_k8_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca32_mvtec_transistor_k8_seed3.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.7830368241920326`
- `auroc`: `0.8154166666666667`
- `brier`: `0.26606217116862413`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.27530489435419436`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0019675443880259992`
- `max_f1`: `0.7076923076923077`
- `model_storage_mb`: `0.4253120422363281`
- `nll`: `0.9581288830650837`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_pca32_mvtec_transistor_k8_seed3_calib_subspace_head_k8_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
