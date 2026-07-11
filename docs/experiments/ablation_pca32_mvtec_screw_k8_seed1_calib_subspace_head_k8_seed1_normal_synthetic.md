# Run ablation_pca32_mvtec_screw_k8_seed1_calib_subspace_head_k8_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca32_mvtec_screw_k8_seed1.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.8660532085324035`
- `auroc`: `0.6835417093666735`
- `brier`: `0.19847475422029223`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.16465565450489522`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.002794997859746218`
- `max_f1`: `0.8656716417910447`
- `model_storage_mb`: `0.4253120422363281`
- `nll`: `0.6205099509843939`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_pca32_mvtec_screw_k8_seed1_calib_subspace_head_k8_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
