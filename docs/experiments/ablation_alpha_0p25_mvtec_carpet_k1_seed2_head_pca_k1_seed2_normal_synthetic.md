# Run ablation_alpha_0p25_mvtec_carpet_k1_seed2_head_pca_k1_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p25_mvtec_carpet_k1_seed2.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9933123817010544`
- `auroc`: `0.9787319422150883`
- `brier`: `0.2078685099518654`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.39198687596198845`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.001811375825578331`
- `max_f1`: `0.9608938547486033`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6083544597028017`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_alpha_0p25_mvtec_carpet_k1_seed2_head_pca_k1_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
