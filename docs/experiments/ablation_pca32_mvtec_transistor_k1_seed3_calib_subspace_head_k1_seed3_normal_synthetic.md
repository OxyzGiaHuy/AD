# Run ablation_pca32_mvtec_transistor_k1_seed3_calib_subspace_head_k1_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca32_mvtec_transistor_k1_seed3.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.7703715157831477`
- `auroc`: `0.80875`
- `brier`: `0.5943561149954779`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.597040758728981`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.004564813990145922`
- `max_f1`: `0.693069306930693`
- `model_storage_mb`: `0.4253120422363281`
- `nll`: `8.509522956685032`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_pca32_mvtec_transistor_k1_seed3_calib_subspace_head_k1_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
