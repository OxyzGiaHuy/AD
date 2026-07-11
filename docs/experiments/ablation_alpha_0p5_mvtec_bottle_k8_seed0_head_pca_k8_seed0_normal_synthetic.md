# Run ablation_alpha_0p5_mvtec_bottle_k8_seed0_head_pca_k8_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p5_mvtec_bottle_k8_seed0.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9968970599783935`
- `auroc`: `0.9904761904761905`
- `brier`: `0.17336890454952086`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.3312462464154484`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.00358735835067479`
- `max_f1`: `0.9767441860465116`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.5352058569398354`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_alpha_0p5_mvtec_bottle_k8_seed0_head_pca_k8_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
