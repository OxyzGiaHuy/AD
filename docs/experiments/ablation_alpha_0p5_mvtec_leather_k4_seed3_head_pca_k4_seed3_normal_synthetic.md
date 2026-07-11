# Run ablation_alpha_0p5_mvtec_leather_k4_seed3_head_pca_k4_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p5_mvtec_leather_k4_seed3.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9980590062111802`
- `auroc`: `0.9932065217391305`
- `brier`: `0.18599756357215738`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.3562739777468865`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.007035797536973992`
- `max_f1`: `0.994535519125683`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.561894026297571`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_alpha_0p5_mvtec_leather_k4_seed3_head_pca_k4_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
