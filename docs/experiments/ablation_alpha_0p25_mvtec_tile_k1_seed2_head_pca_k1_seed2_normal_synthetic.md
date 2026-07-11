# Run ablation_alpha_0p25_mvtec_tile_k1_seed2_head_pca_k1_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p25_mvtec_tile_k1_seed2.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9921529135023093`
- `auroc`: `0.9816017316017316`
- `brier`: `0.22380736962503267`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.37347433021944815`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0024885088682938847`
- `max_f1`: `0.9707602339181286`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6406022816740369`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_alpha_0p25_mvtec_tile_k1_seed2_head_pca_k1_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
