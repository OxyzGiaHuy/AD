# Run ablation_alpha_0p0_mvtec_cable_k1_seed2_head_pca_k1_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p0_mvtec_cable_k1_seed2.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9328021472131383`
- `auroc`: `0.8808095952023988`
- `brier`: `0.24593163216099062`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.12176803549130755`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0029313305020332338`
- `max_f1`: `0.8415841584158416`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6850064199441303`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_alpha_0p0_mvtec_cable_k1_seed2_head_pca_k1_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
