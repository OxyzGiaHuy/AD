# Run ablation_pca64_mvtec_tile_k8_seed1_calib_subspace_head_k8_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca64_mvtec_tile_k8_seed1.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9898483790983981`
- `auroc`: `0.9758297258297258`
- `brier`: `0.1135122430433744`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.13691088386102873`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.003721544837467691`
- `max_f1`: `0.9585798816568047`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `0.4520324676170169`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_pca64_mvtec_tile_k8_seed1_calib_subspace_head_k8_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
