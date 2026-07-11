# Run ablation_alpha_0p75_mvtec_carpet_k8_seed2_head_pca_k8_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p75_mvtec_carpet_k8_seed2.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9974042238522172`
- `auroc`: `0.9915730337078652`
- `brier`: `0.13695731912520615`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.31040587613725257`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0026643298025059905`
- `max_f1`: `0.9723756906077348`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.44911531382321246`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_alpha_0p75_mvtec_carpet_k8_seed2_head_pca_k8_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
