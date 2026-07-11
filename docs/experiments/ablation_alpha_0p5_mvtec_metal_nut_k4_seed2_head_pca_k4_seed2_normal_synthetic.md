# Run ablation_alpha_0p5_mvtec_metal_nut_k4_seed2_head_pca_k4_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p5_mvtec_metal_nut_k4_seed2.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9934618704081792`
- `auroc`: `0.9701857282502444`
- `brier`: `0.1822450343404045`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.21799820557884542`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.002347979467848073`
- `max_f1`: `0.956989247311828`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.5546146964519575`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_alpha_0p5_mvtec_metal_nut_k4_seed2_head_pca_k4_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
