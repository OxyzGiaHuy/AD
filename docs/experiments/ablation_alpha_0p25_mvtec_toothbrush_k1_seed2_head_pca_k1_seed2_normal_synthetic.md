# Run ablation_alpha_0p25_mvtec_toothbrush_k1_seed2_head_pca_k1_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p25_mvtec_toothbrush_k1_seed2.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.962307347512769`
- `auroc`: `0.9`
- `brier`: `0.22685831890740293`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.16485263052440824`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0019359283947518893`
- `max_f1`: `0.8955223880597015`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6466607966904723`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_alpha_0p25_mvtec_toothbrush_k1_seed2_head_pca_k1_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
