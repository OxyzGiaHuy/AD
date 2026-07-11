# Run ablation_alpha_0p75_mvtec_pill_k1_seed0_head_pca_k1_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p75_mvtec_pill_k1_seed0.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9797860087017277`
- `auroc`: `0.9018003273322422`
- `brier`: `0.15782168853488351`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.16593810184273172`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.00237849726157631`
- `max_f1`: `0.9427609427609428`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.5015836290904742`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_alpha_0p75_mvtec_pill_k1_seed0_head_pca_k1_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
