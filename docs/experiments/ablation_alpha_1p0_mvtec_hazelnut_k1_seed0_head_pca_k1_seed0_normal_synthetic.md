# Run ablation_alpha_1p0_mvtec_hazelnut_k1_seed0_head_pca_k1_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_1p0_mvtec_hazelnut_k1_seed0.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9023375779507681`
- `auroc`: `0.7860714285714285`
- `brier`: `0.2388477108763895`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.0873760678551414`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0027084677226164124`
- `max_f1`: `0.8226950354609929`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.673066786286602`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_alpha_1p0_mvtec_hazelnut_k1_seed0_head_pca_k1_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
