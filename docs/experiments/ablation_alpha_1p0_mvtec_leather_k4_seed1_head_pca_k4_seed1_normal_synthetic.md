# Run ablation_alpha_1p0_mvtec_leather_k4_seed1_head_pca_k4_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_1p0_mvtec_leather_k4_seed1.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9908215442475532`
- `auroc`: `0.9697690217391305`
- `brier`: `0.18440017630879538`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.22642853135062802`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0018625807227386582`
- `max_f1`: `0.9497206703910615`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.5536777639483478`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_alpha_1p0_mvtec_leather_k4_seed1_head_pca_k4_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
