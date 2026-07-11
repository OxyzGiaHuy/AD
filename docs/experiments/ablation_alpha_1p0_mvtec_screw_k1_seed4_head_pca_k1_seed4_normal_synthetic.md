# Run ablation_alpha_1p0_mvtec_screw_k1_seed4_head_pca_k1_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_1p0_mvtec_screw_k1_seed4.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.7410614868949235`
- `auroc`: `0.5196761631481861`
- `brier`: `0.19106334305779374`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.019407841935753845`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.00267451434629038`
- `max_f1`: `0.8530465949820788`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.5703000686844232`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_alpha_1p0_mvtec_screw_k1_seed4_head_pca_k1_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
