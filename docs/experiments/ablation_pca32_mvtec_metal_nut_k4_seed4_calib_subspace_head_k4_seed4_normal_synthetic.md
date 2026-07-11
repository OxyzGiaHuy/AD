# Run ablation_pca32_mvtec_metal_nut_k4_seed4_calib_subspace_head_k4_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca32_mvtec_metal_nut_k4_seed4.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9591695540137953`
- `auroc`: `0.8665689149560117`
- `brier`: `0.14782539961401447`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.16092500557070194`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0016817588197148364`
- `max_f1`: `0.9424083769633508`
- `model_storage_mb`: `0.4253120422363281`
- `nll`: `0.6398040633083887`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_pca32_mvtec_metal_nut_k4_seed4_calib_subspace_head_k4_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
