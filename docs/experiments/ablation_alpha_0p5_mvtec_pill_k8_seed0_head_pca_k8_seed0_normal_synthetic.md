# Run ablation_alpha_0p5_mvtec_pill_k8_seed0_head_pca_k8_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p5_mvtec_pill_k8_seed0.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9861300230271213`
- `auroc`: `0.9312602291325696`
- `brier`: `0.16630039816589579`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.2612977927316449`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0019820012531416146`
- `max_f1`: `0.9440559440559441`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.5212696019147902`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_alpha_0p5_mvtec_pill_k8_seed0_head_pca_k8_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
