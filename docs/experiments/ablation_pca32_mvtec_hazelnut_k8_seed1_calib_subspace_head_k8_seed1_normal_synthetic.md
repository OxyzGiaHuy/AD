# Run ablation_pca32_mvtec_hazelnut_k8_seed1_calib_subspace_head_k8_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca32_mvtec_hazelnut_k8_seed1.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9960496776339024`
- `auroc`: `0.9928571428571429`
- `brier`: `0.2774592624503067`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.3082147706638683`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0016611202873966912`
- `max_f1`: `0.9710144927536232`
- `model_storage_mb`: `0.4253120422363281`
- `nll`: `1.340105671331195`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_pca32_mvtec_hazelnut_k8_seed1_calib_subspace_head_k8_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
