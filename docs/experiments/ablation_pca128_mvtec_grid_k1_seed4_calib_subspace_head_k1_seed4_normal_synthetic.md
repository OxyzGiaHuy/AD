# Run ablation_pca128_mvtec_grid_k1_seed4_calib_subspace_head_k1_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca128_mvtec_grid_k1_seed4.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9878170956696294`
- `auroc`: `0.9674185463659147`
- `brier`: `0.2690850222082744`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.269156819734818`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0019620298288571527`
- `max_f1`: `0.95`
- `model_storage_mb`: `0.5659370422363281`
- `nll`: `2.6268229149624025`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_pca128_mvtec_grid_k1_seed4_calib_subspace_head_k1_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
