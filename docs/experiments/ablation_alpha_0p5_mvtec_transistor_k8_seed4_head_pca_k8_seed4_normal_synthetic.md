# Run ablation_alpha_0p5_mvtec_transistor_k8_seed4_head_pca_k8_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p5_mvtec_transistor_k8_seed4.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9494453103061815`
- `auroc`: `0.96375`
- `brier`: `0.2642033068574587`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.22115959703922272`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0034340079873800278`
- `max_f1`: `0.8837209302325582`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.7212025010904098`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_alpha_0p5_mvtec_transistor_k8_seed4_head_pca_k8_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
