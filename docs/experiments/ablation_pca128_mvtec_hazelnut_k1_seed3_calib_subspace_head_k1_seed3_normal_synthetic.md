# Run ablation_pca128_mvtec_hazelnut_k1_seed3_calib_subspace_head_k1_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca128_mvtec_hazelnut_k1_seed3.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9881956309600834`
- `auroc`: `0.98`
- `brier`: `0.3636265248538077`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.3636313568462025`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.002728600376708941`
- `max_f1`: `0.9583333333333334`
- `model_storage_mb`: `0.5659370422363281`
- `nll`: `4.478598932814209`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_pca128_mvtec_hazelnut_k1_seed3_calib_subspace_head_k1_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
