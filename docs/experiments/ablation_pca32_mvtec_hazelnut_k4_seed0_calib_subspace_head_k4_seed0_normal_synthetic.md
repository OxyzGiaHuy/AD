# Run ablation_pca32_mvtec_hazelnut_k4_seed0_calib_subspace_head_k4_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca32_mvtec_hazelnut_k4_seed0.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9771631322290312`
- `auroc`: `0.9567857142857142`
- `brier`: `0.33277409674506797`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.3462638221003792`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.007945621047507633`
- `max_f1`: `0.9185185185185185`
- `model_storage_mb`: `0.4253120422363281`
- `nll`: `1.756925526751329`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_pca32_mvtec_hazelnut_k4_seed0_calib_subspace_head_k4_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
