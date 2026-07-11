# Run ablation_alpha_0p75_mvtec_wood_k8_seed3_head_pca_k8_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p75_mvtec_wood_k8_seed3.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9981518817204301`
- `auroc`: `0.993859649122807`
- `brier`: `0.1790939569962451`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.31595454185823857`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.00405871903500225`
- `max_f1`: `0.9830508474576272`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.5455041623064506`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_alpha_0p75_mvtec_wood_k8_seed3_head_pca_k8_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
