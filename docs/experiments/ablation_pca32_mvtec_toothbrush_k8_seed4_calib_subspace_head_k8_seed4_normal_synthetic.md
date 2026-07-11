# Run ablation_pca32_mvtec_toothbrush_k8_seed4_calib_subspace_head_k8_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca32_mvtec_toothbrush_k8_seed4.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9837444236954042`
- `auroc`: `0.9555555555555556`
- `brier`: `0.17294173877964467`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.19920899612562998`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0026728526378671327`
- `max_f1`: `0.9310344827586207`
- `model_storage_mb`: `0.4253120422363281`
- `nll`: `0.5490864185342055`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_pca32_mvtec_toothbrush_k8_seed4_calib_subspace_head_k8_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
