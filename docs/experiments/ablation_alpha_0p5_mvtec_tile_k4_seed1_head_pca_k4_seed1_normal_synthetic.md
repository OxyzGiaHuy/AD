# Run ablation_alpha_0p5_mvtec_tile_k4_seed1_head_pca_k4_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p5_mvtec_tile_k4_seed1.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9902373070407132`
- `auroc`: `0.974025974025974`
- `brier`: `0.19902263386901867`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.3882258789152162`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0028915444277545325`
- `max_f1`: `0.9700598802395209`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.5889711228089665`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_alpha_0p5_mvtec_tile_k4_seed1_head_pca_k4_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
