# Run ablation_pca16_mvtec_hazelnut_k1_seed3_calib_subspace_head_k1_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca16_mvtec_hazelnut_k1_seed3.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9619232340129494`
- `auroc`: `0.9328571428571428`
- `brier`: `0.3456609425933028`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.3506658841263164`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.002354857325553894`
- `max_f1`: `0.9022556390977443`
- `model_storage_mb`: `0.4018745422363281`
- `nll`: `1.3902399881032925`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_pca16_mvtec_hazelnut_k1_seed3_calib_subspace_head_k1_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
