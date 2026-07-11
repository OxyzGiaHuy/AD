# Run head_pca_mvtec_wood_k4_seed0_head_pca_k4_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/head_pca_mvtec_wood_k4_seed0.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.978614829115624`
- `auroc`: `0.9394736842105263`
- `brier`: `0.2627590488562884`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.302310383018059`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0016586828411002702`
- `max_f1`: `0.9375`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.7185869031849212`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/head_pca_mvtec_wood_k4_seed0_head_pca_k4_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
