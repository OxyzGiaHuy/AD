# Run ablation_pca128_mvtec_carpet_k1_seed4_calib_subspace_head_k1_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca128_mvtec_carpet_k1_seed4.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9997530559328313`
- `auroc`: `0.9991974317817014`
- `brier`: `0.14912670438302458`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.18384867600905583`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0018362029113321223`
- `max_f1`: `0.9943502824858758`
- `model_storage_mb`: `0.5659370422363281`
- `nll`: `0.46415953229052614`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_pca128_mvtec_carpet_k1_seed4_calib_subspace_head_k1_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
