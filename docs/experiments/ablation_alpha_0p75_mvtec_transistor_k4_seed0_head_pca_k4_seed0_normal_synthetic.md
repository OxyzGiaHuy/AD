# Run ablation_alpha_0p75_mvtec_transistor_k4_seed0_head_pca_k4_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p75_mvtec_transistor_k4_seed0.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.8126763569914797`
- `auroc`: `0.83`
- `brier`: `0.31084533647566953`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.277686704993248`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0026194893009960653`
- `max_f1`: `0.7142857142857143`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.8208905226931966`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_alpha_0p75_mvtec_transistor_k4_seed0_head_pca_k4_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
