# Run ablation_pca32_mvtec_transistor_k1_seed1_calib_subspace_head_k1_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca32_mvtec_transistor_k1_seed1.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.8520334266355925`
- `auroc`: `0.885`
- `brier`: `0.5813795044836296`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.5874392926692962`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0021914148144423964`
- `max_f1`: `0.7865168539325843`
- `model_storage_mb`: `0.4253120422363281`
- `nll`: `7.085794806178658`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_pca32_mvtec_transistor_k1_seed1_calib_subspace_head_k1_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
