# Run ablation_pca64_mvtec_tile_k1_seed3_calib_subspace_head_k1_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca64_mvtec_tile_k1_seed3.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9964121218496904`
- `auroc`: `0.9913419913419913`
- `brier`: `0.2693881456964183`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.2752939916064596`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0025532103469993314`
- `max_f1`: `0.9822485207100592`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `1.5603970120541737`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_pca64_mvtec_tile_k1_seed3_calib_subspace_head_k1_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
