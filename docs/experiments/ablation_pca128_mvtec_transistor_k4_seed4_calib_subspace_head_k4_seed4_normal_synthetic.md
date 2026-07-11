# Run ablation_pca128_mvtec_transistor_k4_seed4_calib_subspace_head_k4_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca128_mvtec_transistor_k4_seed4.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9215464554957119`
- `auroc`: `0.9304166666666667`
- `brier`: `0.35163721902278966`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.42392850287258627`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0034563309513032437`
- `max_f1`: `0.8607594936708861`
- `model_storage_mb`: `0.5659370422363281`
- `nll`: `1.2614499468707772`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_pca128_mvtec_transistor_k4_seed4_calib_subspace_head_k4_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
