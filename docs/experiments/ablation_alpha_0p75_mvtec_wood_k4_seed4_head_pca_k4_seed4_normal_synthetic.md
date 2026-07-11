# Run ablation_alpha_0p75_mvtec_wood_k4_seed4_head_pca_k4_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p75_mvtec_wood_k4_seed4.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9974158653846154`
- `auroc`: `0.9912280701754386`
- `brier`: `0.18226676301185663`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.1396927494037001`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.005669128597725796`
- `max_f1`: `0.9830508474576272`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.5515599700843302`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_alpha_0p75_mvtec_wood_k4_seed4_head_pca_k4_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
