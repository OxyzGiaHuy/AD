# Run ablation_alpha_0p5_mvtec_tile_k4_seed0_head_pca_k4_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p5_mvtec_tile_k4_seed0.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9804845202175413`
- `auroc`: `0.9440836940836941`
- `brier`: `0.20289315474121067`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.35350252216697764`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0019594812845317726`
- `max_f1`: `0.9461077844311377`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.5969582356562491`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_alpha_0p5_mvtec_tile_k4_seed0_head_pca_k4_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
