# Run ablation_alpha_1p0_mvtec_hazelnut_k4_seed3_head_pca_k4_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_1p0_mvtec_hazelnut_k4_seed3.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.94045239625101`
- `auroc`: `0.8810714285714286`
- `brier`: `0.23896402492444543`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.09044445048679006`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0032932569526813245`
- `max_f1`: `0.8535031847133758`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6733577965532102`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_alpha_1p0_mvtec_hazelnut_k4_seed3_head_pca_k4_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
