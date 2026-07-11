# Run ablation_alpha_0p5_mvtec_toothbrush_k1_seed4_head_pca_k1_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p5_mvtec_toothbrush_k1_seed4.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9798151404311191`
- `auroc`: `0.9472222222222222`
- `brier`: `0.2087205564317217`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.12420759740329924`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.004705500788986683`
- `max_f1`: `0.9230769230769231`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6089265552401153`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_alpha_0p5_mvtec_toothbrush_k1_seed4_head_pca_k1_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
