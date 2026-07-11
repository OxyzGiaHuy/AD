# Run ablation_alpha_0p5_mvtec_screw_k8_seed0_head_pca_k8_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p5_mvtec_screw_k8_seed0.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9038937119548918`
- `auroc`: `0.804263168682107`
- `brier`: `0.20051465307674493`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.22326459027826784`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.002604071539826691`
- `max_f1`: `0.8770491803278688`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.5922657820885993`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_alpha_0p5_mvtec_screw_k8_seed0_head_pca_k8_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
