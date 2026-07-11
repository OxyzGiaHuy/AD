# Run ablation_alpha_0p25_mvtec_cable_k1_seed4_head_pca_k1_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p25_mvtec_cable_k1_seed4.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9266361758339658`
- `auroc`: `0.8603823088455772`
- `brier`: `0.2376803442410563`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.15361334681510924`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.002241058349609375`
- `max_f1`: `0.8313253012048193`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6684024425546602`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_alpha_0p25_mvtec_cable_k1_seed4_head_pca_k1_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
