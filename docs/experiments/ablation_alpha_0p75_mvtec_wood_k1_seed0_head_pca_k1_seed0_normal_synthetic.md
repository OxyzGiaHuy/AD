# Run ablation_alpha_0p75_mvtec_wood_k1_seed0_head_pca_k1_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p75_mvtec_wood_k1_seed0.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9994489981785064`
- `auroc`: `0.9982456140350877`
- `brier`: `0.17962863898440912`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.1964376229274122`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.005152765072033375`
- `max_f1`: `0.9917355371900827`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.5467790961335267`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_alpha_0p75_mvtec_wood_k1_seed0_head_pca_k1_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
