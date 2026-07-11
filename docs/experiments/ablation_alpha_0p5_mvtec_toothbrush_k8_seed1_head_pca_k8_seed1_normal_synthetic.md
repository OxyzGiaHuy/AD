# Run ablation_alpha_0p5_mvtec_toothbrush_k8_seed1_head_pca_k8_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p5_mvtec_toothbrush_k8_seed1.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9901718930213554`
- `auroc`: `0.975`
- `brier`: `0.20306157530143487`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.32378398094858446`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.004798332894487041`
- `max_f1`: `0.9523809523809523`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.5971717450528116`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_alpha_0p5_mvtec_toothbrush_k8_seed1_head_pca_k8_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
