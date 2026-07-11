# Run ablation_pca128_mvtec_grid_k4_seed4_calib_subspace_head_k4_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca128_mvtec_grid_k4_seed4.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9988003322156941`
- `auroc`: `0.9966583124477861`
- `brier`: `0.25573297298199404`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.26164717246324587`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.002836855892569591`
- `max_f1`: `0.9827586206896551`
- `model_storage_mb`: `0.5659370422363281`
- `nll`: `1.7210225623679605`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_pca128_mvtec_grid_k4_seed4_calib_subspace_head_k4_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
