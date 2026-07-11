# Run ablation_alpha_0p5_mvtec_capsule_k8_seed2_head_pca_k8_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p5_mvtec_capsule_k8_seed2.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9698695529601714`
- `auroc`: `0.879936178699641`
- `brier`: `0.17476433615946146`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.27013475470470655`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.002005462548836614`
- `max_f1`: `0.925764192139738`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.5391639982704226`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_alpha_0p5_mvtec_capsule_k8_seed2_head_pca_k8_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
