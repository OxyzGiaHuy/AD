# Run ablation_alpha_0p75_mvtec_screw_k8_seed2_head_pca_k8_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p75_mvtec_screw_k8_seed2.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.893421337385762`
- `auroc`: `0.7548678007788481`
- `brier`: `0.18546564101138424`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.12044567354023458`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0024001501500606538`
- `max_f1`: `0.8582089552238806`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.5577271108264261`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_alpha_0p75_mvtec_screw_k8_seed2_head_pca_k8_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
