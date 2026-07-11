# Run ablation_pca32_mvtec_carpet_k8_seed1_calib_subspace_head_k8_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca32_mvtec_carpet_k8_seed1.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9989876949123073`
- `auroc`: `0.9967897271268058`
- `brier`: `0.08083355489897182`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.10247998816383058`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0022817829098456944`
- `max_f1`: `0.9887640449438202`
- `model_storage_mb`: `0.4253120422363281`
- `nll`: `0.61183718669259`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_pca32_mvtec_carpet_k8_seed1_calib_subspace_head_k8_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
