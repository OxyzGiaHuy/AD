# Run ablation_pca64_mvtec_transistor_k1_seed2_calib_subspace_head_k1_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca64_mvtec_transistor_k1_seed2.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.745055415868854`
- `auroc`: `0.7941666666666667`
- `brier`: `0.5973637848337338`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.5986078357696533`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0021626470051705838`
- `max_f1`: `0.7`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `5.31306176668897`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_pca64_mvtec_transistor_k1_seed2_calib_subspace_head_k1_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
