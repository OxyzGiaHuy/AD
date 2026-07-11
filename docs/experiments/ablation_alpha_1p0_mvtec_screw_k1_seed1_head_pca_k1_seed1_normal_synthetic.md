# Run ablation_alpha_1p0_mvtec_screw_k1_seed1_head_pca_k1_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_1p0_mvtec_screw_k1_seed1.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.616310877430845`
- `auroc`: `0.5294117647058824`
- `brier`: `0.19111034412087696`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.022906789556145668`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0017071199370548129`
- `max_f1`: `0.8540145985401459`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.5704239104617712`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_alpha_1p0_mvtec_screw_k1_seed1_head_pca_k1_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
