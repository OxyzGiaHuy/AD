# Run ablation_pca32_mvtec_screw_k1_seed4_calib_subspace_head_k1_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca32_mvtec_screw_k1_seed4.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.7810846160455702`
- `auroc`: `0.5937692150030744`
- `brier`: `0.25139453586260635`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.25102010481059556`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0013479653745889664`
- `max_f1`: `0.8679245283018868`
- `model_storage_mb`: `0.4253120422363281`
- `nll`: `1.7285281964326618`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_pca32_mvtec_screw_k1_seed4_calib_subspace_head_k1_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
