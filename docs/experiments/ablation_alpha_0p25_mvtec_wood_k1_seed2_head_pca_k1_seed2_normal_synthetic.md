# Run ablation_alpha_0p25_mvtec_wood_k1_seed2_head_pca_k1_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p25_mvtec_wood_k1_seed2.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9908080356573288`
- `auroc`: `0.968421052631579`
- `brier`: `0.22335406899657528`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.23844239757030827`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.002906352823859529`
- `max_f1`: `0.9572649572649573`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6396491555710836`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_alpha_0p25_mvtec_wood_k1_seed2_head_pca_k1_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
