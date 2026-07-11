# Run ablation_pca16_mvtec_bottle_k1_seed1_calib_subspace_head_k1_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca16_mvtec_bottle_k1_seed1.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9389546655815364`
- `auroc`: `0.8777777777777778`
- `brier`: `0.23243564028505181`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.23651158953287515`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0023481730057532527`
- `max_f1`: `0.9230769230769231`
- `model_storage_mb`: `0.4018745422363281`
- `nll`: `2.006430471552638`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_pca16_mvtec_bottle_k1_seed1_calib_subspace_head_k1_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
