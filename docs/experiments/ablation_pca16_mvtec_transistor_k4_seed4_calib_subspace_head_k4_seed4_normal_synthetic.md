# Run ablation_pca16_mvtec_transistor_k4_seed4_calib_subspace_head_k4_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca16_mvtec_transistor_k4_seed4.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.7715991232074986`
- `auroc`: `0.8308333333333333`
- `brier`: `0.19737983605424053`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.19345779753290118`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0014385893568396569`
- `max_f1`: `0.735632183908046`
- `model_storage_mb`: `0.4018745422363281`
- `nll`: `0.6428741141018475`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_pca16_mvtec_transistor_k4_seed4_calib_subspace_head_k4_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
