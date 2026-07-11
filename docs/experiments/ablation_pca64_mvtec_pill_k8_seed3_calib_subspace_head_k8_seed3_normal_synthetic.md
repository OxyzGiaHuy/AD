# Run ablation_pca64_mvtec_pill_k8_seed3_calib_subspace_head_k8_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca64_mvtec_pill_k8_seed3.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9896800173063391`
- `auroc`: `0.9509001636661211`
- `brier`: `0.062093325672170824`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.0554152232863868`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0017600001176138838`
- `max_f1`: `0.9577464788732394`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `0.24303485940903582`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_pca64_mvtec_pill_k8_seed3_calib_subspace_head_k8_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
