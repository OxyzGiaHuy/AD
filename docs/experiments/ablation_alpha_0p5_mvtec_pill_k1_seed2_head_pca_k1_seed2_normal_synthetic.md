# Run ablation_alpha_0p5_mvtec_pill_k1_seed2_head_pca_k1_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p5_mvtec_pill_k1_seed2.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9828357171878743`
- `auroc`: `0.9138025095471904`
- `brier`: `0.17749936729871382`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.23962217355202778`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0017666873817672273`
- `max_f1`: `0.9427609427609428`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.5452037985336929`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_alpha_0p5_mvtec_pill_k1_seed2_head_pca_k1_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
