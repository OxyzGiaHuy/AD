# Run ablation_pca16_mvtec_grid_k4_seed4_calib_subspace_head_k4_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca16_mvtec_grid_k4_seed4.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9078593337839816`
- `auroc`: `0.7936507936507936`
- `brier`: `0.21454104597375667`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.19950855809908644`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0035172785417391704`
- `max_f1`: `0.9090909090909091`
- `model_storage_mb`: `0.4018745422363281`
- `nll`: `0.7011728566010123`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_pca16_mvtec_grid_k4_seed4_calib_subspace_head_k4_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
