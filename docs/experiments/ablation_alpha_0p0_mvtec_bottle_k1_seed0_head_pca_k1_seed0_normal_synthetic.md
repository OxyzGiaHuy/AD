# Run ablation_alpha_0p0_mvtec_bottle_k1_seed0_head_pca_k1_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p0_mvtec_bottle_k1_seed0.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9820928868310992`
- `auroc`: `0.9626984126984127`
- `brier`: `0.2493462083981435`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.35099613846066485`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0028477793402341476`
- `max_f1`: `0.9763779527559056`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6918241645915262`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_alpha_0p0_mvtec_bottle_k1_seed0_head_pca_k1_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
