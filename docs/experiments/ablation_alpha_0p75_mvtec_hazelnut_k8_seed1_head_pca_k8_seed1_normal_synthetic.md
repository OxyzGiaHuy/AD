# Run ablation_alpha_0p75_mvtec_hazelnut_k8_seed1_head_pca_k8_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p75_mvtec_hazelnut_k8_seed1.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9889760385813018`
- `auroc`: `0.9735714285714285`
- `brier`: `0.22608776042706027`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.10648857030001557`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0035230016166513615`
- `max_f1`: `0.9705882352941176`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6433301925079593`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_alpha_0p75_mvtec_hazelnut_k8_seed1_head_pca_k8_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
