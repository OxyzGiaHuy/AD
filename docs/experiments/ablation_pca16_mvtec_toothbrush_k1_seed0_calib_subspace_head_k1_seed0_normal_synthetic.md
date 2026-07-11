# Run ablation_pca16_mvtec_toothbrush_k1_seed0_calib_subspace_head_k1_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca16_mvtec_toothbrush_k1_seed0.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9713024052059335`
- `auroc`: `0.925`
- `brier`: `0.13818965774687864`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.14839642980535112`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.003478831389830226`
- `max_f1`: `0.90625`
- `model_storage_mb`: `0.4018745422363281`
- `nll`: `0.6589443972323732`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_pca16_mvtec_toothbrush_k1_seed0_calib_subspace_head_k1_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
