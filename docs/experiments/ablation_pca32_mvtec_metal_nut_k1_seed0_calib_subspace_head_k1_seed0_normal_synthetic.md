# Run ablation_pca32_mvtec_metal_nut_k1_seed0_calib_subspace_head_k1_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca32_mvtec_metal_nut_k1_seed0.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9760053362291853`
- `auroc`: `0.9110459433040078`
- `brier`: `0.176416226814915`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.1792887002877567`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0019150337285321693`
- `max_f1`: `0.9417989417989417`
- `model_storage_mb`: `0.4253120422363281`
- `nll`: `1.8838034040674296`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_pca32_mvtec_metal_nut_k1_seed0_calib_subspace_head_k1_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
