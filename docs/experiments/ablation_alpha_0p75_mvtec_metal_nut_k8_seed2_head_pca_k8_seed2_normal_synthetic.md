# Run ablation_alpha_0p75_mvtec_metal_nut_k8_seed2_head_pca_k8_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p75_mvtec_metal_nut_k8_seed2.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9934534432184637`
- `auroc`: `0.9731182795698925`
- `brier`: `0.15583152631737296`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.244768084132153`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0034439831648183906`
- `max_f1`: `0.9735449735449735`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.49513970775002347`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_alpha_0p75_mvtec_metal_nut_k8_seed2_head_pca_k8_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
