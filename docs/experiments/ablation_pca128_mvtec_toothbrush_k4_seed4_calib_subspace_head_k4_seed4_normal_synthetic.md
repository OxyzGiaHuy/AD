# Run ablation_pca128_mvtec_toothbrush_k4_seed4_calib_subspace_head_k4_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca128_mvtec_toothbrush_k4_seed4.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9853017495420165`
- `auroc`: `0.9638888888888889`
- `brier`: `0.23043395157763277`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.25396894273303805`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0043741414057356974`
- `max_f1`: `0.9523809523809523`
- `model_storage_mb`: `0.5659370422363281`
- `nll`: `1.3738938733584558`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_pca128_mvtec_toothbrush_k4_seed4_calib_subspace_head_k4_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
