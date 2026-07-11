# Run ablation_alpha_0p0_mvtec_screw_k4_seed0_head_pca_k4_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p0_mvtec_screw_k4_seed0.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.8767219844008135`
- `auroc`: `0.7493338798934208`
- `brier`: `0.26852609900659885`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.28642470613121984`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.003374563786201179`
- `max_f1`: `0.8905660377358491`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.7302673661455128`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_alpha_0p0_mvtec_screw_k4_seed0_head_pca_k4_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
