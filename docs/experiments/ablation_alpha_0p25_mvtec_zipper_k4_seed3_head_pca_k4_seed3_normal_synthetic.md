# Run ablation_alpha_0p25_mvtec_zipper_k4_seed3_head_pca_k4_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p25_mvtec_zipper_k4_seed3.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9841923029065927`
- `auroc`: `0.9438025210084033`
- `brier`: `0.19875748443407754`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.3468986244391132`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0033122815981211254`
- `max_f1`: `0.9558232931726908`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.5896453853333997`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_alpha_0p25_mvtec_zipper_k4_seed3_head_pca_k4_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
