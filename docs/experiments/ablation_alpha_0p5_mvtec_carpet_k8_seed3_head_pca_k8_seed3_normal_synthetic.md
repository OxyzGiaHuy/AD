# Run ablation_alpha_0p5_mvtec_carpet_k8_seed3_head_pca_k8_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p5_mvtec_carpet_k8_seed3.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9936879201193044`
- `auroc`: `0.9791332263242376`
- `brier`: `0.17687924536632396`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.3457203418271154`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0030231647129751677`
- `max_f1`: `0.9666666666666667`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.5434639036491005`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_alpha_0p5_mvtec_carpet_k8_seed3_head_pca_k8_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
