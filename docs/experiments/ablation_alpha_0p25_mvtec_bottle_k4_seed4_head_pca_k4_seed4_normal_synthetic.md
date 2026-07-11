# Run ablation_alpha_0p25_mvtec_bottle_k4_seed4_head_pca_k4_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p25_mvtec_bottle_k4_seed4.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9962788381859412`
- `auroc`: `0.9880952380952381`
- `brier`: `0.2127773651039749`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.4078981815332391`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0021963380950402065`
- `max_f1`: `0.9692307692307692`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6183179968719904`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_alpha_0p25_mvtec_bottle_k4_seed4_head_pca_k4_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
