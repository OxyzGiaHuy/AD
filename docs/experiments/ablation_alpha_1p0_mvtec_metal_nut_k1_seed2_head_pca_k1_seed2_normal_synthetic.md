# Run ablation_alpha_1p0_mvtec_metal_nut_k1_seed2_head_pca_k1_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_1p0_mvtec_metal_nut_k1_seed2.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.964801820707401`
- `auroc`: `0.8800097751710655`
- `brier`: `0.1623181796680709`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.09064680856207141`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0021474740427473316`
- `max_f1`: `0.9387755102040817`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.508562880826445`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_alpha_1p0_mvtec_metal_nut_k1_seed2_head_pca_k1_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
