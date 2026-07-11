# Run ablation_pca128_mvtec_hazelnut_k4_seed4_calib_subspace_head_k4_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca128_mvtec_hazelnut_k4_seed4.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9912837522378461`
- `auroc`: `0.9860714285714286`
- `brier`: `0.3550838309564124`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.3591003954410554`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0022425094280730594`
- `max_f1`: `0.9790209790209791`
- `model_storage_mb`: `0.5659370422363281`
- `nll`: `2.2286779622332813`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_pca128_mvtec_hazelnut_k4_seed4_calib_subspace_head_k4_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
