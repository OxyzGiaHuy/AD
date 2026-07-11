# Run ablation_alpha_0p75_mvtec_tile_k1_seed2_head_pca_k1_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p75_mvtec_tile_k1_seed2.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9908885334630863`
- `auroc`: `0.977994227994228`
- `brier`: `0.1926034240683737`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.33594264841487265`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0026018314986911593`
- `max_f1`: `0.9651162790697675`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.5737337385480082`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_alpha_0p75_mvtec_tile_k1_seed2_head_pca_k1_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
