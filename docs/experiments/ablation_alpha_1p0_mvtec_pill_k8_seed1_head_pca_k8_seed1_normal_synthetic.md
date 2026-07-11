# Run ablation_alpha_1p0_mvtec_pill_k8_seed1_head_pca_k8_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_1p0_mvtec_pill_k8_seed1.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9830627593618217`
- `auroc`: `0.9484451718494271`
- `brier`: `0.12328866374039969`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.1877255243455579`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0029033094332246725`
- `max_f1`: `0.971830985915493`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.41471982258315704`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_alpha_1p0_mvtec_pill_k8_seed1_head_pca_k8_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
