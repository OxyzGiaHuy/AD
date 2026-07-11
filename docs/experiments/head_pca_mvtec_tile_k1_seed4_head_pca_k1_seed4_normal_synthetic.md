# Run head_pca_mvtec_tile_k1_seed4_head_pca_k1_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/head_pca_mvtec_tile_k1_seed4.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9964121218496904`
- `auroc`: `0.9913419913419913`
- `brier`: `0.2502488656176799`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.42734725582293975`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0016040834956444227`
- `max_f1`: `0.9822485207100592`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6936118735710053`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/head_pca_mvtec_tile_k1_seed4_head_pca_k1_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
