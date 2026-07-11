# Run ablation_alpha_1p0_mvtec_screw_k4_seed2_head_pca_k4_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_1p0_mvtec_screw_k4_seed2.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.8934780614166554`
- `auroc`: `0.7409305185488829`
- `brier`: `0.18914893804816818`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.07029279060661794`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.002420664846431464`
- `max_f1`: `0.8603773584905661`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.5654938851271203`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_alpha_1p0_mvtec_screw_k4_seed2_head_pca_k4_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
