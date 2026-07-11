# Run ablation_pca16_mvtec_zipper_k4_seed4_calib_subspace_head_k4_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca16_mvtec_zipper_k4_seed4.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9895221202954294`
- `auroc`: `0.961922268907563`
- `brier`: `0.06798032263511804`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.07035243302423329`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0019381854880527155`
- `max_f1`: `0.9508196721311475`
- `model_storage_mb`: `0.4018745422363281`
- `nll`: `0.21898047226244127`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_pca16_mvtec_zipper_k4_seed4_calib_subspace_head_k4_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
