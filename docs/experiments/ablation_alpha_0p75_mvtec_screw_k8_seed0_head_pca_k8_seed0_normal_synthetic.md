# Run ablation_alpha_0p75_mvtec_screw_k8_seed0_head_pca_k8_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p75_mvtec_screw_k8_seed0.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9051521145866671`
- `auroc`: `0.803238368518139`
- `brier`: `0.1908302913895463`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.13149283565580844`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.00237469628918916`
- `max_f1`: `0.8674698795180723`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.5707743405363132`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_alpha_0p75_mvtec_screw_k8_seed0_head_pca_k8_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
