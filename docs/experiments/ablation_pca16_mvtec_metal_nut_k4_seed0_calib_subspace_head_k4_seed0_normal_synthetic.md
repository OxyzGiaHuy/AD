# Run ablation_pca16_mvtec_metal_nut_k4_seed0_calib_subspace_head_k4_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca16_mvtec_metal_nut_k4_seed0.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.916408022499697`
- `auroc`: `0.7702834799608993`
- `brier`: `0.10929051861644754`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.1081365312895049`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0013555273413658141`
- `max_f1`: `0.9292929292929293`
- `model_storage_mb`: `0.4018745422363281`
- `nll`: `0.5665011200861049`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_pca16_mvtec_metal_nut_k4_seed0_calib_subspace_head_k4_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
