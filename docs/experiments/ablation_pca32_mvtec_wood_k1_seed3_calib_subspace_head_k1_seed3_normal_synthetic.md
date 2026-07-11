# Run ablation_pca32_mvtec_wood_k1_seed3_calib_subspace_head_k1_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca32_mvtec_wood_k1_seed3.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9848644251366644`
- `auroc`: `0.9570175438596491`
- `brier`: `0.24046387143461562`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.24048509024366538`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0023402860741826553`
- `max_f1`: `0.957983193277311`
- `model_storage_mb`: `0.4253120422363281`
- `nll`: `3.458148885513158`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_pca32_mvtec_wood_k1_seed3_calib_subspace_head_k1_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
