# Run ablation_alpha_0p0_mvtec_cable_k4_seed0_head_pca_k4_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p0_mvtec_cable_k4_seed0.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9516331822653253`
- `auroc`: `0.9072338830584707`
- `brier`: `0.24227716205783176`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.34453965644041695`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0026917935907840728`
- `max_f1`: `0.8876404494382022`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.677649780373733`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_alpha_0p0_mvtec_cable_k4_seed0_head_pca_k4_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
