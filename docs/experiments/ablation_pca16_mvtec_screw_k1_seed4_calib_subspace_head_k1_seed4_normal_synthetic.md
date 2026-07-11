# Run ablation_pca16_mvtec_screw_k1_seed4_calib_subspace_head_k1_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca16_mvtec_screw_k1_seed4.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.7888897844382576`
- `auroc`: `0.5453986472637835`
- `brier`: `0.3222344737868945`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.31891755795800664`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0019450750784017145`
- `max_f1`: `0.8530465949820788`
- `model_storage_mb`: `0.4018745422363281`
- `nll`: `2.4094871778958376`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_pca16_mvtec_screw_k1_seed4_calib_subspace_head_k1_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
