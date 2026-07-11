# Run ablation_alpha_0p75_mvtec_zipper_k8_seed0_head_pca_k8_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p75_mvtec_zipper_k8_seed0.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9825682873173635`
- `auroc`: `0.9375`
- `brier`: `0.1563114084730137`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.19889949962792816`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.003809644883831605`
- `max_f1`: `0.943089430894309`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.49448317678699666`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_alpha_0p75_mvtec_zipper_k8_seed0_head_pca_k8_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
