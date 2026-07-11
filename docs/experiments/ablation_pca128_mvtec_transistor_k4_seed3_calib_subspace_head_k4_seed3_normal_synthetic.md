# Run ablation_pca128_mvtec_transistor_k4_seed3_calib_subspace_head_k4_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca128_mvtec_transistor_k4_seed3.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.8524491544497528`
- `auroc`: `0.8916666666666667`
- `brier`: `0.345458398029143`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.4046532771363854`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0020129269734025`
- `max_f1`: `0.8292682926829268`
- `model_storage_mb`: `0.5659370422363281`
- `nll`: `1.6877943557886557`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_pca128_mvtec_transistor_k4_seed3_calib_subspace_head_k4_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
