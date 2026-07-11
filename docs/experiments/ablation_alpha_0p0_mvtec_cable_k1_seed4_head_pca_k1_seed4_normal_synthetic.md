# Run ablation_alpha_0p0_mvtec_cable_k1_seed4_head_pca_k1_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p0_mvtec_cable_k1_seed4.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.931379596429638`
- `auroc`: `0.8680659670164917`
- `brier`: `0.24973111170753726`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.17150586525599157`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.003057855392495791`
- `max_f1`: `0.847457627118644`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6926002543624776`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_alpha_0p0_mvtec_cable_k1_seed4_head_pca_k1_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
