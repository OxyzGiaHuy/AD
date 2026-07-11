# Run ablation_alpha_0p25_mvtec_hazelnut_k4_seed4_head_pca_k4_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p25_mvtec_hazelnut_k4_seed4.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9776802682533264`
- `auroc`: `0.955`
- `brier`: `0.22872702198866773`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.17169910181652423`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.002906278148293495`
- `max_f1`: `0.9305555555555556`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.65030513107806`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_alpha_0p25_mvtec_hazelnut_k4_seed4_head_pca_k4_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
