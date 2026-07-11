# Run ablation_alpha_0p75_mvtec_pill_k1_seed2_head_pca_k1_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p75_mvtec_pill_k1_seed2.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9816713366218568`
- `auroc`: `0.9072558647026732`
- `brier`: `0.15679374799595946`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.2022521149612473`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0019201191287197754`
- `max_f1`: `0.9355932203389831`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.4993011584910122`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_alpha_0p75_mvtec_pill_k1_seed2_head_pca_k1_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
