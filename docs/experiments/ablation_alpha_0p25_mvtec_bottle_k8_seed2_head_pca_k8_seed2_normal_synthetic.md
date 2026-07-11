# Run ablation_alpha_0p25_mvtec_bottle_k8_seed2_head_pca_k8_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p25_mvtec_bottle_k8_seed2.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9888220985708541`
- `auroc`: `0.969047619047619`
- `brier`: `0.2074743805165397`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.39146149481635484`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.002028872202857431`
- `max_f1`: `0.9682539682539683`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6076038780831772`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_alpha_0p25_mvtec_bottle_k8_seed2_head_pca_k8_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
