# Run ablation_alpha_1p0_mvtec_tile_k1_seed2_head_pca_k1_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_1p0_mvtec_tile_k1_seed2.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9930425520013709`
- `auroc`: `0.9808802308802309`
- `brier`: `0.18946943478066916`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.08041393604034038`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0020000961505704457`
- `max_f1`: `0.9575757575757575`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.5648556770018104`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_alpha_1p0_mvtec_tile_k1_seed2_head_pca_k1_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
