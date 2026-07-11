# Run ablation_alpha_0p5_mvtec_tile_k1_seed1_head_pca_k1_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p5_mvtec_tile_k1_seed1.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9764241214565491`
- `auroc`: `0.93001443001443`
- `brier`: `0.2068667097051297`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.3380056268129593`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0025731449166678973`
- `max_f1`: `0.9182389937106918`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6053129344037808`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_alpha_0p5_mvtec_tile_k1_seed1_head_pca_k1_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
