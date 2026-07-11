# Run ablation_alpha_0p25_mvtec_hazelnut_k4_seed0_head_pca_k4_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p25_mvtec_hazelnut_k4_seed0.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9672317335358672`
- `auroc`: `0.9417857142857143`
- `brier`: `0.22746490719684892`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.08077239773490213`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0020367442884228447`
- `max_f1`: `0.92`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6476326585626729`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_alpha_0p25_mvtec_hazelnut_k4_seed0_head_pca_k4_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
