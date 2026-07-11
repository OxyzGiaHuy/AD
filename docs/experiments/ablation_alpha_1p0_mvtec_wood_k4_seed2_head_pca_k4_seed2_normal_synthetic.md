# Run ablation_alpha_1p0_mvtec_wood_k4_seed2_head_pca_k4_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_1p0_mvtec_wood_k4_seed2.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9970472118010877`
- `auroc`: `0.9899122807017544`
- `brier`: `0.17983334617624122`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.24626458445681804`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.002893610845638227`
- `max_f1`: `0.9833333333333333`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.5448212037253988`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_alpha_1p0_mvtec_wood_k4_seed2_head_pca_k4_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
