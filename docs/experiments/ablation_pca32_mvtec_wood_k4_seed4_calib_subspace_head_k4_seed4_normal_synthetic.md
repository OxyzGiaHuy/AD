# Run ablation_pca32_mvtec_wood_k4_seed4_calib_subspace_head_k4_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca32_mvtec_wood_k4_seed4.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9845605904687567`
- `auroc`: `0.9535087719298245`
- `brier`: `0.15801086709922837`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.17965280632429487`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.00257095817146422`
- `max_f1`: `0.9391304347826087`
- `model_storage_mb`: `0.4253120422363281`
- `nll`: `1.245100448973307`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_pca32_mvtec_wood_k4_seed4_calib_subspace_head_k4_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
