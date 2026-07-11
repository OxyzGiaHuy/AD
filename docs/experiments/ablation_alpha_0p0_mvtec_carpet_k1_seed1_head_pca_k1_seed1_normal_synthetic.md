# Run ablation_alpha_0p0_mvtec_carpet_k1_seed1_head_pca_k1_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p0_mvtec_carpet_k1_seed1.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9992505332590388`
- `auroc`: `0.9975922953451043`
- `brier`: `0.2366914543137732`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.4207407855070554`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0026351180978310415`
- `max_f1`: `0.9887640449438202`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.666491678028225`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_alpha_0p0_mvtec_carpet_k1_seed1_head_pca_k1_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
