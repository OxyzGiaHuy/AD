# Run ablation_pca64_mvtec_hazelnut_k1_seed3_calib_subspace_head_k1_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca64_mvtec_hazelnut_k1_seed3.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9981950417535854`
- `auroc`: `0.9967857142857143`
- `brier`: `0.3636345137343599`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.3636354370550676`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.004925866425037384`
- `max_f1`: `0.9787234042553191`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `5.1524339629648095`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_pca64_mvtec_hazelnut_k1_seed3_calib_subspace_head_k1_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
