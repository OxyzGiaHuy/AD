# Run ablation_alpha_1p0_mvtec_metal_nut_k1_seed1_head_pca_k1_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_1p0_mvtec_metal_nut_k1_seed1.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9565388740928776`
- `auroc`: `0.8167155425219942`
- `brier`: `0.1616974873198983`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.08679440539816152`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0020766781076141027`
- `max_f1`: `0.8985507246376812`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.5070166102689541`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_alpha_1p0_mvtec_metal_nut_k1_seed1_head_pca_k1_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
