# Run ablation_alpha_0p25_mvtec_screw_k8_seed4_head_pca_k8_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p25_mvtec_screw_k8_seed4.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.8986412461878862`
- `auroc`: `0.7763886042221767`
- `brier`: `0.21570443117179455`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.21321122013032437`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0024185587302781642`
- `max_f1`: `0.873015873015873`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6239818841306564`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_alpha_0p25_mvtec_screw_k8_seed4_head_pca_k8_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
