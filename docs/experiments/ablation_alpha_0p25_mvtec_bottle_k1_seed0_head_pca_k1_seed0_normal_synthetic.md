# Run ablation_alpha_0p25_mvtec_bottle_k1_seed0_head_pca_k1_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p25_mvtec_bottle_k1_seed0.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9809060752942648`
- `auroc`: `0.95`
- `brier`: `0.21797099299512288`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.3906109832137464`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.003810707928545504`
- `max_f1`: `0.96`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6288328923182713`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_alpha_0p25_mvtec_bottle_k1_seed0_head_pca_k1_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
