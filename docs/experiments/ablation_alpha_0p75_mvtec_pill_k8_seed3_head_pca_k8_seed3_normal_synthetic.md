# Run ablation_alpha_0p75_mvtec_pill_k8_seed3_head_pca_k8_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p75_mvtec_pill_k8_seed3.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9849380516463957`
- `auroc`: `0.9263502454991817`
- `brier`: `0.14260452927595751`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.23252639727678134`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.002019824103234771`
- `max_f1`: `0.9484536082474226`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.46716932442587106`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_alpha_0p75_mvtec_pill_k8_seed3_head_pca_k8_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
