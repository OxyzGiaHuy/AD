# Run ablation_alpha_0p25_mvtec_toothbrush_k8_seed0_head_pca_k8_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p25_mvtec_toothbrush_k8_seed0.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9889881763085786`
- `auroc`: `0.9722222222222222`
- `brier`: `0.210855720517988`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.2972616539114997`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.004748430768293994`
- `max_f1`: `0.9523809523809523`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6141534830712599`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_alpha_0p25_mvtec_toothbrush_k8_seed0_head_pca_k8_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
