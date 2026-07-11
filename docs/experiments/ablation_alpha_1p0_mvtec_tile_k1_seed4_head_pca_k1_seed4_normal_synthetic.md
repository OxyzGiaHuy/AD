# Run ablation_alpha_1p0_mvtec_tile_k1_seed4_head_pca_k1_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_1p0_mvtec_tile_k1_seed4.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9615496905054199`
- `auroc`: `0.88997113997114`
- `brier`: `0.19736383301885704`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.0347977087029025`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0020389568665598193`
- `max_f1`: `0.8860759493670886`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.5824234909915359`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_alpha_1p0_mvtec_tile_k1_seed4_head_pca_k1_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
