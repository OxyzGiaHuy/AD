# Run ablation_alpha_0p25_mvtec_screw_k8_seed0_head_pca_k8_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p25_mvtec_screw_k8_seed0.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9046591549950675`
- `auroc`: `0.8124615699938512`
- `brier`: `0.2175726164746865`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.2586604723706842`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0031499064643867314`
- `max_f1`: `0.8925619834710744`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6278778052682454`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_alpha_0p25_mvtec_screw_k8_seed0_head_pca_k8_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
