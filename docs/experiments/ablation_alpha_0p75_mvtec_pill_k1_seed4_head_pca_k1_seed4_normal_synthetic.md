# Run ablation_alpha_0p75_mvtec_pill_k1_seed4_head_pca_k1_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p75_mvtec_pill_k1_seed4.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9380776548994813`
- `auroc`: `0.707583196944899`
- `brier`: `0.15982287899184733`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.17067136628899024`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0025565127011187776`
- `max_f1`: `0.9185667752442996`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.5061411874223212`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_alpha_0p75_mvtec_pill_k1_seed4_head_pca_k1_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
