# Run ablation_alpha_0p75_mvtec_transistor_k8_seed4_head_pca_k8_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p75_mvtec_transistor_k8_seed4.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9504170737041271`
- `auroc`: `0.9616666666666667`
- `brier`: `0.2946100435484106`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.2706298148632049`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0028593834675848485`
- `max_f1`: `0.8536585365853658`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.78495702021619`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_alpha_0p75_mvtec_transistor_k8_seed4_head_pca_k8_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
