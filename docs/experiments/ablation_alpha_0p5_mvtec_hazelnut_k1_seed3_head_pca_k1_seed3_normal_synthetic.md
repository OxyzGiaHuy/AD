# Run ablation_alpha_0p5_mvtec_hazelnut_k1_seed3_head_pca_k1_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p5_mvtec_hazelnut_k1_seed3.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9883678584751469`
- `auroc`: `0.9728571428571429`
- `brier`: `0.22807224941871712`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.021821907433596466`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0019550060176036573`
- `max_f1`: `0.9635036496350365`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6484583697028096`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_alpha_0p5_mvtec_hazelnut_k1_seed3_head_pca_k1_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
