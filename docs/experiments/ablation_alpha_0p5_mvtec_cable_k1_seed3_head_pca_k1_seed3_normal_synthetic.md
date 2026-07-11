# Run ablation_alpha_0p5_mvtec_cable_k1_seed3_head_pca_k1_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p5_mvtec_cable_k1_seed3.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9430412410112676`
- `auroc`: `0.8913043478260869`
- `brier`: `0.23393978067993576`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.07357753197352099`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.00205819151053826`
- `max_f1`: `0.8587570621468926`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6604942146239313`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_alpha_0p5_mvtec_cable_k1_seed3_head_pca_k1_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
