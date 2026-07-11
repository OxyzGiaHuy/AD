# Run head_pca_mvtec_grid_k1_seed4_head_pca_k1_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/head_pca_mvtec_grid_k1_seed4.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9949224602742585`
- `auroc`: `0.985797827903091`
- `brier`: `0.2538365671124078`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.3461310275090046`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0016565344845637297`
- `max_f1`: `0.9655172413793104`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.7008074907181336`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/head_pca_mvtec_grid_k1_seed4_head_pca_k1_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
