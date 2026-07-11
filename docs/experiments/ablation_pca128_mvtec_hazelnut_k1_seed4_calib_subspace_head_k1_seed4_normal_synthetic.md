# Run ablation_pca128_mvtec_hazelnut_k1_seed4_calib_subspace_head_k1_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca128_mvtec_hazelnut_k1_seed4.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9772741930193434`
- `auroc`: `0.965`
- `brier`: `0.3634536086376081`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.3635439520532435`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.002681172198869965`
- `max_f1`: `0.9452054794520548`
- `model_storage_mb`: `0.5659370422363281`
- `nll`: `3.5546972715943714`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_pca128_mvtec_hazelnut_k1_seed4_calib_subspace_head_k1_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
