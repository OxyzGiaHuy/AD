# Run ablation_alpha_0p25_mvtec_toothbrush_k8_seed2_head_pca_k8_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p25_mvtec_toothbrush_k8_seed2.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9849034811437481`
- `auroc`: `0.9611111111111111`
- `brier`: `0.21615375882706656`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.20263140967914034`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0034579775695289883`
- `max_f1`: `0.9508196721311475`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.624923626889979`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_alpha_0p25_mvtec_toothbrush_k8_seed2_head_pca_k8_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
