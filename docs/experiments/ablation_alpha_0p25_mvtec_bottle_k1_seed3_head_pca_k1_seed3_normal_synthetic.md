# Run ablation_alpha_0p25_mvtec_bottle_k1_seed3_head_pca_k1_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p25_mvtec_bottle_k1_seed3.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9958871380045136`
- `auroc`: `0.9865079365079366`
- `brier`: `0.21504029979099318`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.26515620192849493`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0021904457180973993`
- `max_f1`: `0.967741935483871`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6228054664991253`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_alpha_0p25_mvtec_bottle_k1_seed3_head_pca_k1_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
