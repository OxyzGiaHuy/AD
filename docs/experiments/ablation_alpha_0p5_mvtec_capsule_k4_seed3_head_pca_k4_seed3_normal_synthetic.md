# Run ablation_alpha_0p5_mvtec_capsule_k4_seed3_head_pca_k4_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p5_mvtec_capsule_k4_seed3.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9665328912075368`
- `auroc`: `0.8591942560829677`
- `brier`: `0.17701423154280035`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.2316645487691417`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0026235572965533443`
- `max_f1`: `0.9316239316239316`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.5438373569326508`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_alpha_0p5_mvtec_capsule_k4_seed3_head_pca_k4_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
