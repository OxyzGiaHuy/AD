# Run ablation_pca128_mvtec_transistor_k1_seed2_calib_subspace_head_k1_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca128_mvtec_transistor_k1_seed2.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.760322501708418`
- `auroc`: `0.80875`
- `brier`: `0.5964265913855671`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.5980078864097595`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.002310687731951475`
- `max_f1`: `0.7111111111111111`
- `model_storage_mb`: `0.5659370422363281`
- `nll`: `4.287483615021977`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_pca128_mvtec_transistor_k1_seed2_calib_subspace_head_k1_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
