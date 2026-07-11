# Run ablation_alpha_0p0_mvtec_pill_k1_seed0_head_pca_k1_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p0_mvtec_pill_k1_seed0.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9820660333432175`
- `auroc`: `0.9129841789416258`
- `brier`: `0.24768755216308017`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.3471737213120489`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0026739433430090637`
- `max_f1`: `0.9488054607508533`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6885192606187102`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_alpha_0p0_mvtec_pill_k1_seed0_head_pca_k1_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
