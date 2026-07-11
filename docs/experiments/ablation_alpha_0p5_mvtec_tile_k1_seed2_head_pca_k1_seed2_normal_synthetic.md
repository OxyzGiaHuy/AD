# Run ablation_alpha_0p5_mvtec_tile_k1_seed2_head_pca_k1_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p5_mvtec_tile_k1_seed2.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9919900245043545`
- `auroc`: `0.9812409812409812`
- `brier`: `0.2030651341177174`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.3768992041930174`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0018974623491621425`
- `max_f1`: `0.9710982658959537`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.5975419811188993`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_alpha_0p5_mvtec_tile_k1_seed2_head_pca_k1_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
