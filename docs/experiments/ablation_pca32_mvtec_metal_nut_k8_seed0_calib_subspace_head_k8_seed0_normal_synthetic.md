# Run ablation_pca32_mvtec_metal_nut_k8_seed0_calib_subspace_head_k8_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca32_mvtec_metal_nut_k8_seed0.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9600629297501857`
- `auroc`: `0.8729227761485826`
- `brier`: `0.10286241883018869`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.10699203822599801`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.001748130972618642`
- `max_f1`: `0.9435897435897436`
- `model_storage_mb`: `0.4253120422363281`
- `nll`: `0.6105044683598035`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_pca32_mvtec_metal_nut_k8_seed0_calib_subspace_head_k8_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
