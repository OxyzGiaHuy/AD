# Run ablation_alpha_0p75_mvtec_pill_k1_seed3_head_pca_k1_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p75_mvtec_pill_k1_seed3.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9693203400652832`
- `auroc`: `0.8518821603927987`
- `brier`: `0.15827815066394046`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.1840231297258846`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.003140801508091167`
- `max_f1`: `0.9319727891156463`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.5026372088862621`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_alpha_0p75_mvtec_pill_k1_seed3_head_pca_k1_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
