# Run ablation_pca16_mvtec_toothbrush_k1_seed3_calib_subspace_head_k1_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca16_mvtec_toothbrush_k1_seed3.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9844104839448685`
- `auroc`: `0.9611111111111111`
- `brier`: `0.24597462679915`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.2620476597831362`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0033147229946085383`
- `max_f1`: `0.9508196721311475`
- `model_storage_mb`: `0.4018745422363281`
- `nll`: `1.9199080834778532`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_pca16_mvtec_toothbrush_k1_seed3_calib_subspace_head_k1_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
