# Run ablation_pca128_mvtec_tile_k8_seed4_calib_subspace_head_k8_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca128_mvtec_tile_k8_seed4.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9930263265832556`
- `auroc`: `0.9837662337662337`
- `brier`: `0.058334529128737295`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.07571918483123055`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0018892484820551341`
- `max_f1`: `0.9764705882352941`
- `model_storage_mb`: `0.5659370422363281`
- `nll`: `0.26999488612328876`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_pca128_mvtec_tile_k8_seed4_calib_subspace_head_k8_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
