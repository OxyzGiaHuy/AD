# Run ablation_alpha_0p75_mvtec_tile_k4_seed4_head_pca_k4_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p75_mvtec_tile_k4_seed4.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9916539425412687`
- `auroc`: `0.9797979797979798`
- `brier`: `0.1897105471297034`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.22066129119987157`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0020893276470084475`
- `max_f1`: `0.9764705882352941`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.5662184998456966`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_alpha_0p75_mvtec_tile_k4_seed4_head_pca_k4_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
