# Run ablation_alpha_1p0_mvtec_hazelnut_k4_seed0_head_pca_k4_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_1p0_mvtec_hazelnut_k4_seed0.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9466049369543311`
- `auroc`: `0.8882142857142857`
- `brier`: `0.24196137185853078`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.10364539298144253`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.004628090204840357`
- `max_f1`: `0.8702290076335878`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6809835492331063`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_alpha_1p0_mvtec_hazelnut_k4_seed0_head_pca_k4_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
