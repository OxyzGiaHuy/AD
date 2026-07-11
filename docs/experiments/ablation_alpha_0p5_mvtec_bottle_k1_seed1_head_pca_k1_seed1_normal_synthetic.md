# Run ablation_alpha_0p5_mvtec_bottle_k1_seed1_head_pca_k1_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p5_mvtec_bottle_k1_seed1.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9768009522271198`
- `auroc`: `0.9380952380952381`
- `brier`: `0.19815172634978248`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.22905985562198136`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.002640131322375263`
- `max_f1`: `0.9465648854961832`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.5874230011653253`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_alpha_0p5_mvtec_bottle_k1_seed1_head_pca_k1_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
