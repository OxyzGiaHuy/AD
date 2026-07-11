# Run ablation_alpha_0p0_mvtec_hazelnut_k8_seed4_head_pca_k8_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p0_mvtec_hazelnut_k8_seed4.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9947469153378441`
- `auroc`: `0.9921428571428571`
- `brier`: `0.23826679047139207`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.16806131655519654`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0026716952804814688`
- `max_f1`: `0.9929078014184397`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.669660305808198`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_alpha_0p0_mvtec_hazelnut_k8_seed4_head_pca_k8_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
