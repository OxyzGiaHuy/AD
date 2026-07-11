# Run ablation_alpha_0p75_mvtec_wood_k8_seed2_head_pca_k8_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p75_mvtec_wood_k8_seed2.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9900270768711021`
- `auroc`: `0.9710526315789474`
- `brier`: `0.17518560193616126`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.10192078276525568`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.002146458347575574`
- `max_f1`: `0.9672131147540983`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.5346746119912362`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_alpha_0p75_mvtec_wood_k8_seed2_head_pca_k8_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
