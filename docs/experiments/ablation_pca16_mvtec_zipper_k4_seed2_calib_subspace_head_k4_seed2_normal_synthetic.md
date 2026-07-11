# Run ablation_pca16_mvtec_zipper_k4_seed2_calib_subspace_head_k4_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca16_mvtec_zipper_k4_seed2.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9696201981685716`
- `auroc`: `0.8983718487394958`
- `brier`: `0.09846776059398878`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.11607096927388517`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0021732645787742753`
- `max_f1`: `0.9397590361445783`
- `model_storage_mb`: `0.4018745422363281`
- `nll`: `0.6733460433682195`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_pca16_mvtec_zipper_k4_seed2_calib_subspace_head_k4_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
