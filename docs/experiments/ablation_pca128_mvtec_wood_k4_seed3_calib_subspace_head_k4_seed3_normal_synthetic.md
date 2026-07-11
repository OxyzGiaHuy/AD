# Run ablation_pca128_mvtec_wood_k4_seed3_calib_subspace_head_k4_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca128_mvtec_wood_k4_seed3.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9935473340309038`
- `auroc`: `0.9789473684210527`
- `brier`: `0.16828391592637104`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.19523381356951555`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0017631599042989032`
- `max_f1`: `0.9661016949152542`
- `model_storage_mb`: `0.5659370422363281`
- `nll`: `1.05002565907185`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_pca128_mvtec_wood_k4_seed3_calib_subspace_head_k4_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
