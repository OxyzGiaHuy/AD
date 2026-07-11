# Run ablation_alpha_1p0_mvtec_cable_k1_seed4_head_pca_k1_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_1p0_mvtec_cable_k1_seed4.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.7837769198095866`
- `auroc`: `0.6633245877061469`
- `brier`: `0.24780992315290917`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.10324227690696719`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0037551583970586457`
- `max_f1`: `0.7634854771784232`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6919083667357262`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_alpha_1p0_mvtec_cable_k1_seed4_head_pca_k1_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
