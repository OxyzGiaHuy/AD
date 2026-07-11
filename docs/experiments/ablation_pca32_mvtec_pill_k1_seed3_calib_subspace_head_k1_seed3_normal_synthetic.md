# Run ablation_pca32_mvtec_pill_k1_seed3_calib_subspace_head_k1_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca32_mvtec_pill_k1_seed3.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9771285126701761`
- `auroc`: `0.886797599563557`
- `brier`: `0.15562712335634693`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.15565224678930412`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0013368348897752648`
- `max_f1`: `0.9324324324324325`
- `model_storage_mb`: `0.4253120422363281`
- `nll`: `1.7222902627958194`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_pca32_mvtec_pill_k1_seed3_calib_subspace_head_k1_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
