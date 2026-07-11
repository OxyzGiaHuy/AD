# Run ablation_alpha_0p25_mvtec_transistor_k1_seed1_head_pca_k1_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p25_mvtec_transistor_k1_seed1.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.8428897488615078`
- `auroc`: `0.8308333333333333`
- `brier`: `0.25721505620879587`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.1458787530660629`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.002661972958594561`
- `max_f1`: `0.7647058823529411`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.7075716371110918`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_alpha_0p25_mvtec_transistor_k1_seed1_head_pca_k1_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
