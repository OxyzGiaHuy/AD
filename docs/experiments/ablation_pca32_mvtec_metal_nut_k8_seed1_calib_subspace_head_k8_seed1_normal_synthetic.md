# Run ablation_pca32_mvtec_metal_nut_k8_seed1_calib_subspace_head_k8_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca32_mvtec_metal_nut_k8_seed1.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9889496595790572`
- `auroc`: `0.9560117302052786`
- `brier`: `0.11507268849678565`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.1304256051211901`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.002655252134022505`
- `max_f1`: `0.9528795811518325`
- `model_storage_mb`: `0.4253120422363281`
- `nll`: `0.642992315013445`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_pca32_mvtec_metal_nut_k8_seed1_calib_subspace_head_k8_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
