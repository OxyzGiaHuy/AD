# Run ablation_alpha_0p5_mvtec_pill_k1_seed1_head_pca_k1_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p5_mvtec_pill_k1_seed1.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9813424273320972`
- `auroc`: `0.9118930714675395`
- `brier`: `0.17731688150551966`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.2436280885856308`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0026884804184208375`
- `max_f1`: `0.9455782312925171`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.5448126952259529`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_alpha_0p5_mvtec_pill_k1_seed1_head_pca_k1_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
