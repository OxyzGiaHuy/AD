# Run ablation_alpha_0p75_mvtec_bottle_k8_seed4_head_pca_k8_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p75_mvtec_bottle_k8_seed4.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9957888820686885`
- `auroc`: `0.9873015873015873`
- `brier`: `0.17193346475238577`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.26006367623087867`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.005032392039176929`
- `max_f1`: `0.9763779527559056`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.5296009054606339`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_alpha_0p75_mvtec_bottle_k8_seed4_head_pca_k8_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
