# Run ablation_pca16_mvtec_hazelnut_k8_seed3_calib_subspace_head_k8_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca16_mvtec_hazelnut_k8_seed3.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9184838476175514`
- `auroc`: `0.8585714285714285`
- `brier`: `0.24126293370692128`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.2576385496692224`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0030093725262717768`
- `max_f1`: `0.8518518518518519`
- `model_storage_mb`: `0.4018745422363281`
- `nll`: `0.9612971015019999`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_pca16_mvtec_hazelnut_k8_seed3_calib_subspace_head_k8_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
