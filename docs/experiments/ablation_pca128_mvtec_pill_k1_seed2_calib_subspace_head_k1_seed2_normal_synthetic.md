# Run ablation_pca128_mvtec_pill_k1_seed2_calib_subspace_head_k1_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca128_mvtec_pill_k1_seed2.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9871872519402174`
- `auroc`: `0.933442444080742`
- `brier`: `0.15342104789044603`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.15428498762096476`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0023080545427378064`
- `max_f1`: `0.95`
- `model_storage_mb`: `0.5659370422363281`
- `nll`: `0.9557865655261383`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_pca128_mvtec_pill_k1_seed2_calib_subspace_head_k1_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
