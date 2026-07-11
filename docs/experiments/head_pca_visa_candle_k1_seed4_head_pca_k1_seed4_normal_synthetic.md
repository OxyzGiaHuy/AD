# Run head_pca_visa_candle_k1_seed4_head_pca_k1_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/visa_full/head_pca_visa_candle_k1_seed4.yaml`
- Dataset: `visa`
- Model: `head_pca`

## Metrics

- `ap`: `0.8599097277425901`
- `auroc`: `0.8622`
- `brier`: `0.24108398219662022`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.0023429246246814946`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.008882315745577216`
- `max_f1`: `0.8019323671497585`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6753050389800268`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/head_pca_visa_candle_k1_seed4_head_pca_k1_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
