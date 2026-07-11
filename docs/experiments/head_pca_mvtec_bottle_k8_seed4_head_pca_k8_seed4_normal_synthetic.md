# Run head_pca_mvtec_bottle_k8_seed4_head_pca_k8_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/head_pca_mvtec_bottle_k8_seed4.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9967916942976308`
- `auroc`: `0.9904761904761905`
- `brier`: `0.251287421759165`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.35903969909771377`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0016467944909650159`
- `max_f1`: `0.984375`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6956311018333311`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/head_pca_mvtec_bottle_k8_seed4_head_pca_k8_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
