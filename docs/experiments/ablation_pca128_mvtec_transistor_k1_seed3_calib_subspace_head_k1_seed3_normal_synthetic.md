# Run ablation_pca128_mvtec_transistor_k1_seed3_calib_subspace_head_k1_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca128_mvtec_transistor_k1_seed3.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.7911871316849759`
- `auroc`: `0.8245833333333333`
- `brier`: `0.5962915995409834`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.598031011223793`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0025320132821798325`
- `max_f1`: `0.6987951807228916`
- `model_storage_mb`: `0.5659370422363281`
- `nll`: `4.822744383785043`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_pca128_mvtec_transistor_k1_seed3_calib_subspace_head_k1_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
