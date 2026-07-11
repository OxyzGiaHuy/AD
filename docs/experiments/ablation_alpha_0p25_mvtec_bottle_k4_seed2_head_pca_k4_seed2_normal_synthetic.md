# Run ablation_alpha_0p25_mvtec_bottle_k4_seed2_head_pca_k4_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p25_mvtec_bottle_k4_seed2.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9951440148892859`
- `auroc`: `0.9865079365079366`
- `brier`: `0.2076039573238516`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.37563902426914997`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.004348629950938454`
- `max_f1`: `0.9921259842519685`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6077807793771979`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_alpha_0p25_mvtec_bottle_k4_seed2_head_pca_k4_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
