# Run ablation_pca64_mvtec_transistor_k4_seed1_calib_subspace_head_k4_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca64_mvtec_transistor_k4_seed1.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.7625609398358252`
- `auroc`: `0.7975`
- `brier`: `0.44716239613550685`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.4929402592778206`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.002090939227491617`
- `max_f1`: `0.6851851851851852`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `2.479303510594086`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_pca64_mvtec_transistor_k4_seed1_calib_subspace_head_k4_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
