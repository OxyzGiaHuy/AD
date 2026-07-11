# Run ablation_pca128_mvtec_zipper_k4_seed2_calib_subspace_head_k4_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca128_mvtec_zipper_k4_seed2.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9749907433479417`
- `auroc`: `0.9125525210084033`
- `brier`: `0.13355421005195883`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.15141567034609865`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0021811747763133206`
- `max_f1`: `0.9322709163346613`
- `model_storage_mb`: `0.5659370422363281`
- `nll`: `0.7525717741670084`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_pca128_mvtec_zipper_k4_seed2_calib_subspace_head_k4_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
