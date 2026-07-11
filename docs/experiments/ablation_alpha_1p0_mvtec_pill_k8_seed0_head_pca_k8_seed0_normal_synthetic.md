# Run ablation_alpha_1p0_mvtec_pill_k8_seed0_head_pca_k8_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_1p0_mvtec_pill_k8_seed0.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9774309997595851`
- `auroc`: `0.9078014184397163`
- `brier`: `0.12431899015268731`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.111728697836756`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0026635381610629087`
- `max_f1`: `0.9366197183098591`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.415799702748968`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_alpha_1p0_mvtec_pill_k8_seed0_head_pca_k8_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
