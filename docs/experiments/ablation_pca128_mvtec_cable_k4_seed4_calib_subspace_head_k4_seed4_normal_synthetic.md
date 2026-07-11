# Run ablation_pca128_mvtec_cable_k4_seed4_calib_subspace_head_k4_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca128_mvtec_cable_k4_seed4.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9513176185658591`
- `auroc`: `0.902736131934033`
- `brier`: `0.3400639542822646`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.3539039451877276`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0036140879119435946`
- `max_f1`: `0.8823529411764706`
- `model_storage_mb`: `0.5659370422363281`
- `nll`: `1.8899580997035934`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_pca128_mvtec_cable_k4_seed4_calib_subspace_head_k4_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
