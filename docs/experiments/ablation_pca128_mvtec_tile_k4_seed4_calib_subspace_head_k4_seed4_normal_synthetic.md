# Run ablation_pca128_mvtec_tile_k4_seed4_calib_subspace_head_k4_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca128_mvtec_tile_k4_seed4.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9967330182838516`
- `auroc`: `0.9924242424242424`
- `brier`: `0.07143794166354729`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.10844351394245251`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0025594406562228487`
- `max_f1`: `0.9882352941176471`
- `model_storage_mb`: `0.5659370422363281`
- `nll`: `0.29757355318987555`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_pca128_mvtec_tile_k4_seed4_calib_subspace_head_k4_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
