# Run ablation_alpha_0p75_mvtec_cable_k1_seed4_head_pca_k1_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p75_mvtec_cable_k1_seed4.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9162706771889089`
- `auroc`: `0.8408920539730135`
- `brier`: `0.23860441644515398`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.2555760979652405`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0017238318795959155`
- `max_f1`: `0.8202247191011236`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6703372435381237`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_alpha_0p75_mvtec_cable_k1_seed4_head_pca_k1_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
