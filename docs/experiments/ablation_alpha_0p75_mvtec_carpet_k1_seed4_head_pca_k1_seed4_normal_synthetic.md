# Run ablation_alpha_0p75_mvtec_carpet_k1_seed4_head_pca_k1_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p75_mvtec_carpet_k1_seed4.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.982115000071816`
- `auroc`: `0.9333868378812199`
- `brier`: `0.1674304435245842`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.29003133350967336`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0032898102465093644`
- `max_f1`: `0.9364161849710982`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.5209944413084039`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_alpha_0p75_mvtec_carpet_k1_seed4_head_pca_k1_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
