# Run ablation_alpha_0p5_mvtec_bottle_k4_seed1_head_pca_k4_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p5_mvtec_bottle_k4_seed1.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9974441920054349`
- `auroc`: `0.9920634920634921`
- `brier`: `0.18811045450969244`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.3201976389770049`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.003090674102485898`
- `max_f1`: `0.984375`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.5663152178838604`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_alpha_0p5_mvtec_bottle_k4_seed1_head_pca_k4_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
