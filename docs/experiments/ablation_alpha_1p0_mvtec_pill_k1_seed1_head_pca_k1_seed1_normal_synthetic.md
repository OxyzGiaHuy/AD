# Run ablation_alpha_1p0_mvtec_pill_k1_seed1_head_pca_k1_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_1p0_mvtec_pill_k1_seed1.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9406344591738381`
- `auroc`: `0.7768685215493726`
- `brier`: `0.14560606493331557`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.1236014947919788`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0019190571867598745`
- `max_f1`: `0.9328859060402684`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.4723815674913452`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_alpha_1p0_mvtec_pill_k1_seed1_head_pca_k1_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
