# Run ablation_alpha_1p0_mvtec_wood_k1_seed4_head_pca_k1_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_1p0_mvtec_wood_k1_seed4.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9746680162038294`
- `auroc`: `0.9219298245614035`
- `brier`: `0.18063885917955327`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.05751462375061426`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.002689862222988394`
- `max_f1`: `0.9243697478991597`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.5472313938617361`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_alpha_1p0_mvtec_wood_k1_seed4_head_pca_k1_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
