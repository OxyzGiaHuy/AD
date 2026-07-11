# Run ablation_alpha_0p75_mvtec_transistor_k1_seed0_head_pca_k1_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p75_mvtec_transistor_k1_seed0.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.8129397676161088`
- `auroc`: `0.8258333333333333`
- `brier`: `0.31379549750780755`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.2744267648458481`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.003294319994747639`
- `max_f1`: `0.735632183908046`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.8274154227137928`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_alpha_0p75_mvtec_transistor_k1_seed0_head_pca_k1_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
