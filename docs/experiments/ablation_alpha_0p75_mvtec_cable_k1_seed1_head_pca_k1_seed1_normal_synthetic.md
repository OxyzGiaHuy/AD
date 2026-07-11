# Run ablation_alpha_0p75_mvtec_cable_k1_seed1_head_pca_k1_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p75_mvtec_cable_k1_seed1.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.8839539788044996`
- `auroc`: `0.8007871064467766`
- `brier`: `0.23915642426031344`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.05717066884040836`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0026372027148803077`
- `max_f1`: `0.8036529680365296`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6715698311552558`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_alpha_0p75_mvtec_cable_k1_seed1_head_pca_k1_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
