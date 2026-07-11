# Run ablation_pca64_mvtec_transistor_k4_seed0_calib_subspace_head_k4_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca64_mvtec_transistor_k4_seed0.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.8087076470048611`
- `auroc`: `0.84375`
- `brier`: `0.45513253856943775`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.49889299243688584`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0014880943857133388`
- `max_f1`: `0.75`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `2.201822394409852`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_pca64_mvtec_transistor_k4_seed0_calib_subspace_head_k4_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
