# Run ablation_pca16_mvtec_screw_k4_seed1_calib_subspace_head_k4_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca16_mvtec_screw_k4_seed1.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.8382464646165423`
- `auroc`: `0.6202090592334495`
- `brier`: `0.23046719415956568`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.23169832569546997`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0023606269853189586`
- `max_f1`: `0.8530465949820788`
- `model_storage_mb`: `0.4018745422363281`
- `nll`: `0.7582675250749424`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_pca16_mvtec_screw_k4_seed1_calib_subspace_head_k4_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
