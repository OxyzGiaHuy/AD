# Run ablation_pca64_mvtec_hazelnut_k1_seed4_calib_subspace_head_k1_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca64_mvtec_hazelnut_k1_seed4.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9810531602027097`
- `auroc`: `0.97`
- `brier`: `0.3636339458966976`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.36363515474579555`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0019100992686369202`
- `max_f1`: `0.951048951048951`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `5.949213590839374`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_pca64_mvtec_hazelnut_k1_seed4_calib_subspace_head_k1_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
