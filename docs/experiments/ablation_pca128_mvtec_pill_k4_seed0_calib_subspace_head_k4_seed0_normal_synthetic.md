# Run ablation_pca128_mvtec_pill_k4_seed0_calib_subspace_head_k4_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca128_mvtec_pill_k4_seed0.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9911331847960428`
- `auroc`: `0.955810147299509`
- `brier`: `0.08164319317903994`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.09397574485151357`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0021361155312753723`
- `max_f1`: `0.9652777777777778`
- `model_storage_mb`: `0.5659370422363281`
- `nll`: `0.32851114598835857`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_pca128_mvtec_pill_k4_seed0_calib_subspace_head_k4_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
