# Run ablation_alpha_0p25_mvtec_screw_k4_seed3_head_pca_k4_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p25_mvtec_screw_k4_seed3.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.8711569197443784`
- `auroc`: `0.7661406025824964`
- `brier`: `0.21921472230445477`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.24886480011045925`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.00234346273355186`
- `max_f1`: `0.8880597014925373`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6312100200039696`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_alpha_0p25_mvtec_screw_k4_seed3_head_pca_k4_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
