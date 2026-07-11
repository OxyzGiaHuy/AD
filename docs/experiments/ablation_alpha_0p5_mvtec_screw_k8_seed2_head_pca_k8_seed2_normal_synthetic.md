# Run ablation_alpha_0p5_mvtec_screw_k8_seed2_head_pca_k8_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p5_mvtec_screw_k8_seed2.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.8974387422194293`
- `auroc`: `0.7671654027464644`
- `brier`: `0.19817326257038043`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.18087505660951136`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.002598243171814829`
- `max_f1`: `0.864`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.5871515355808787`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_alpha_0p5_mvtec_screw_k8_seed2_head_pca_k8_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
