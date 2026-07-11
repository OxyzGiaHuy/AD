# Run ablation_pca16_mvtec_grid_k4_seed1_calib_subspace_head_k4_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca16_mvtec_grid_k4_seed1.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9967833194912991`
- `auroc`: `0.9908103592314118`
- `brier`: `0.18236882245157182`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.2261761203408241`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.003263888713450004`
- `max_f1`: `0.9734513274336283`
- `model_storage_mb`: `0.4018745422363281`
- `nll`: `0.5106513985962143`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_pca16_mvtec_grid_k4_seed1_calib_subspace_head_k4_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
