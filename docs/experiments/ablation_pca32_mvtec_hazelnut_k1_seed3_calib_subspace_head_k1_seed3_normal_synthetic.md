# Run ablation_pca32_mvtec_hazelnut_k1_seed3_calib_subspace_head_k1_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca32_mvtec_hazelnut_k1_seed3.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9955790219372963`
- `auroc`: `0.9917857142857143`
- `brier`: `0.3636360276835168`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.36363619565963745`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0023637659339742225`
- `max_f1`: `0.965034965034965`
- `model_storage_mb`: `0.4253120422363281`
- `nll`: `6.015795228814886`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_pca32_mvtec_hazelnut_k1_seed3_calib_subspace_head_k1_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
