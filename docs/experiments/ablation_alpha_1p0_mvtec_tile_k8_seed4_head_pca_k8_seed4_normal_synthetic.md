# Run ablation_alpha_1p0_mvtec_tile_k8_seed4_head_pca_k8_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_1p0_mvtec_tile_k8_seed4.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9881748473053455`
- `auroc`: `0.9704184704184704`
- `brier`: `0.18272528149311737`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.21748954567134887`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.00305360374160302`
- `max_f1`: `0.9467455621301775`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.5468703515809222`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_alpha_1p0_mvtec_tile_k8_seed4_head_pca_k8_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
