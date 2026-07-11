# Run head_pca_mvtec_bottle_k2_seed1_head_pca_k2_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/head_pca_mvtec_bottle_k2_seed1.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.985990028441933`
- `auroc`: `0.9634920634920635`
- `brier`: `0.2520947310901848`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.38946873919073355`
- `k_shot`: `2`
- `latency_sec_per_image`: `0.0016446653304688901`
- `max_f1`: `0.96875`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.697295724448675`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `2738`

## Notes

- Predictions written to outputs/head_pca_mvtec_bottle_k2_seed1_head_pca_k2_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
