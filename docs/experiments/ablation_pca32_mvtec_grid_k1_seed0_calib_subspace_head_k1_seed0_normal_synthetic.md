# Run ablation_pca32_mvtec_grid_k1_seed0_calib_subspace_head_k1_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca32_mvtec_grid_k1_seed0.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9882643874441189`
- `auroc`: `0.9649122807017544`
- `brier`: `0.26922927304429795`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.2692300211160611`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0013902116901217364`
- `max_f1`: `0.9380530973451328`
- `model_storage_mb`: `0.4253120422363281`
- `nll`: `4.724940012076358`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_pca32_mvtec_grid_k1_seed0_calib_subspace_head_k1_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
