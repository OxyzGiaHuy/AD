# Run ablation_alpha_0p5_mvtec_metal_nut_k8_seed0_head_pca_k8_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p5_mvtec_metal_nut_k8_seed0.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9914305267737883`
- `auroc`: `0.9672531769305963`
- `brier`: `0.17320164681223346`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.2911561281784721`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.005026120692491531`
- `max_f1`: `0.9732620320855615`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.5354489371906938`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_alpha_0p5_mvtec_metal_nut_k8_seed0_head_pca_k8_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
