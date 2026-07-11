# Run ablation_alpha_1p0_mvtec_carpet_k1_seed1_head_pca_k1_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_1p0_mvtec_carpet_k1_seed1.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9808102676025477`
- `auroc`: `0.9301765650080257`
- `brier`: `0.16088173858308988`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.2052308947612077`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0018996186236031035`
- `max_f1`: `0.9341317365269461`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.5035853685037972`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_alpha_1p0_mvtec_carpet_k1_seed1_head_pca_k1_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
