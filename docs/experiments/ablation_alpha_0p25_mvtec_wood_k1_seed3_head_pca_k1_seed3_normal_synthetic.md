# Run ablation_alpha_0p25_mvtec_wood_k1_seed3_head_pca_k1_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p25_mvtec_wood_k1_seed3.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9849276582474018`
- `auroc`: `0.9578947368421052`
- `brier`: `0.22062785263327425`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.27566312687306466`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0022653217274176923`
- `max_f1`: `0.9586776859504132`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6341421722149001`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_alpha_0p25_mvtec_wood_k1_seed3_head_pca_k1_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
