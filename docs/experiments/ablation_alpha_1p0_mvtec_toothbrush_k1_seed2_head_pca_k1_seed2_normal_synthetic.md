# Run ablation_alpha_1p0_mvtec_toothbrush_k1_seed2_head_pca_k1_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_1p0_mvtec_toothbrush_k1_seed2.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9552399618261688`
- `auroc`: `0.7875`
- `brier`: `0.20419150825924087`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.01052740783918471`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0019039699275578772`
- `max_f1`: `0.9032258064516129`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.5985428743434504`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_alpha_1p0_mvtec_toothbrush_k1_seed2_head_pca_k1_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
