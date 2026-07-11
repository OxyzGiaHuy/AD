# Run ablation_pca128_mvtec_transistor_k8_seed0_calib_subspace_head_k8_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca128_mvtec_transistor_k8_seed0.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.8524481764227311`
- `auroc`: `0.8816666666666667`
- `brier`: `0.20538253486171235`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.22862346009118478`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0025851850770413874`
- `max_f1`: `0.7951807228915663`
- `model_storage_mb`: `0.5659370422363281`
- `nll`: `0.7756770716220734`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_pca128_mvtec_transistor_k8_seed0_calib_subspace_head_k8_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
