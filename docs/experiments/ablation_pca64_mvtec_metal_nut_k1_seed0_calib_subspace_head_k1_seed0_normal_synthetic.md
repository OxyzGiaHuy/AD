# Run ablation_pca64_mvtec_metal_nut_k1_seed0_calib_subspace_head_k1_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca64_mvtec_metal_nut_k1_seed0.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9875564983308118`
- `auroc`: `0.9491691104594331`
- `brier`: `0.18764509108112382`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.18929641402286038`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0016210508087406987`
- `max_f1`: `0.9484536082474226`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `1.5437526584833283`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_pca64_mvtec_metal_nut_k1_seed0_calib_subspace_head_k1_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
