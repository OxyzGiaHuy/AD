# Run ablation_alpha_0p75_mvtec_cable_k4_seed1_head_pca_k4_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p75_mvtec_cable_k4_seed1.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9539180079231293`
- `auroc`: `0.9083583208395802`
- `brier`: `0.23646497230311123`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.07863512436548875`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.00347080380966266`
- `max_f1`: `0.8875739644970414`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6651665054774196`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_alpha_0p75_mvtec_cable_k4_seed1_head_pca_k4_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
