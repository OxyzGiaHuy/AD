# Run ablation_alpha_1p0_mvtec_screw_k4_seed3_head_pca_k4_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_1p0_mvtec_screw_k4_seed3.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.8006651350381377`
- `auroc`: `0.6003279360524698`
- `brier`: `0.1877027097371333`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.0741663444787263`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.002623307891190052`
- `max_f1`: `0.8689138576779026`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.5619224017808706`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_alpha_1p0_mvtec_screw_k4_seed3_head_pca_k4_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
