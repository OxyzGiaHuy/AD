# Run ablation_pca128_mvtec_capsule_k1_seed3_calib_subspace_head_k1_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca128_mvtec_capsule_k1_seed3.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9621323392147793`
- `auroc`: `0.8556043079377742`
- `brier`: `0.17204146061047665`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.17272313661647565`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0018728339451957834`
- `max_f1`: `0.9279279279279279`
- `model_storage_mb`: `0.5659370422363281`
- `nll`: `1.189372097254027`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_pca128_mvtec_capsule_k1_seed3_calib_subspace_head_k1_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
