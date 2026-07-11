# Run ablation_alpha_0p0_mvtec_pill_k4_seed3_head_pca_k4_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p0_mvtec_pill_k4_seed3.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9894953829303893`
- `auroc`: `0.9487179487179487`
- `brier`: `0.2403287609885891`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.39248587556941783`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0027871514018067345`
- `max_f1`: `0.9583333333333334`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6737766702663447`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_alpha_0p0_mvtec_pill_k4_seed3_head_pca_k4_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
