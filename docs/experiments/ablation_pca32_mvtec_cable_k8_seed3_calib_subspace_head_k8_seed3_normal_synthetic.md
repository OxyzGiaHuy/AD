# Run ablation_pca32_mvtec_cable_k8_seed3_calib_subspace_head_k8_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca32_mvtec_cable_k8_seed3.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9220275755163732`
- `auroc`: `0.8577586206896551`
- `brier`: `0.25821588547323054`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.26921919293701646`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0015994839494427044`
- `max_f1`: `0.8272251308900523`
- `model_storage_mb`: `0.4253120422363281`
- `nll`: `1.0406437551471508`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_pca32_mvtec_cable_k8_seed3_calib_subspace_head_k8_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
