# Run ablation_alpha_0p25_mvtec_hazelnut_k1_seed0_head_pca_k1_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p25_mvtec_hazelnut_k1_seed0.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9616602824493355`
- `auroc`: `0.9196428571428571`
- `brier`: `0.23330799346983677`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.08277410756457937`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0025275100191885775`
- `max_f1`: `0.8920863309352518`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6595636001005399`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_alpha_0p25_mvtec_hazelnut_k1_seed0_head_pca_k1_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
