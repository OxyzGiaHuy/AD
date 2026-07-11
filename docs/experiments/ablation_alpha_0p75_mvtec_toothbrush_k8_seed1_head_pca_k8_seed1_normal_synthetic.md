# Run ablation_alpha_0p75_mvtec_toothbrush_k8_seed1_head_pca_k8_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p75_mvtec_toothbrush_k8_seed1.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9875565084059709`
- `auroc`: `0.9694444444444444`
- `brier`: `0.1950416262893549`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.1561421822933924`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.003873197938359919`
- `max_f1`: `0.9523809523809523`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.5780644383457195`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_alpha_0p75_mvtec_toothbrush_k8_seed1_head_pca_k8_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
