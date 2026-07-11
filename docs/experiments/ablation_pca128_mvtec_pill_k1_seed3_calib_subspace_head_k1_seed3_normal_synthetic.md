# Run ablation_pca128_mvtec_pill_k1_seed3_calib_subspace_head_k1_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca128_mvtec_pill_k1_seed3.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.972335981360099`
- `auroc`: `0.8696126568466994`
- `brier`: `0.1553243328693945`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.15542854556066543`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0017720299165048998`
- `max_f1`: `0.936026936026936`
- `model_storage_mb`: `0.5659370422363281`
- `nll`: `1.2622162332394906`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_pca128_mvtec_pill_k1_seed3_calib_subspace_head_k1_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
