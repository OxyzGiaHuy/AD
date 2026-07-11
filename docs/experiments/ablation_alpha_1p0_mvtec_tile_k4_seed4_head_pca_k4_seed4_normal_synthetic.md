# Run ablation_alpha_1p0_mvtec_tile_k4_seed4_head_pca_k4_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_1p0_mvtec_tile_k4_seed4.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9921486413379568`
- `auroc`: `0.9805194805194806`
- `brier`: `0.1904647044428486`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.20202663107814953`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.005056020716189319`
- `max_f1`: `0.9761904761904762`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.565318523220007`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_alpha_1p0_mvtec_tile_k4_seed4_head_pca_k4_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
