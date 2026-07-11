# Run ablation_alpha_1p0_mvtec_screw_k8_seed3_head_pca_k8_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_1p0_mvtec_screw_k8_seed3.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.8794505060253677`
- `auroc`: `0.7515884402541504`
- `brier`: `0.18409293909384014`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.11570676527917381`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.002708070201333612`
- `max_f1`: `0.8812260536398467`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.5530606292513314`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_alpha_1p0_mvtec_screw_k8_seed3_head_pca_k8_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
