# Run ablation_alpha_0p5_mvtec_metal_nut_k8_seed3_head_pca_k8_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p5_mvtec_metal_nut_k8_seed3.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9991938454248434`
- `auroc`: `0.9965786901270772`
- `brier`: `0.17748344723826884`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.3389966840329378`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0019852453599805415`
- `max_f1`: `0.989247311827957`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.5448189871726812`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_alpha_0p5_mvtec_metal_nut_k8_seed3_head_pca_k8_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
