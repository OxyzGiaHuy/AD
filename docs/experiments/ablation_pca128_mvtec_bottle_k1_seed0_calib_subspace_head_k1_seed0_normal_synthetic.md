# Run ablation_pca128_mvtec_bottle_k1_seed0_calib_subspace_head_k1_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca128_mvtec_bottle_k1_seed0.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.981787288691885`
- `auroc`: `0.9571428571428572`
- `brier`: `0.23804055583812475`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.23945813940232064`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0020118058625474035`
- `max_f1`: `0.9606299212598425`
- `model_storage_mb`: `0.5659370422363281`
- `nll`: `1.548880600340845`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_pca128_mvtec_bottle_k1_seed0_calib_subspace_head_k1_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
