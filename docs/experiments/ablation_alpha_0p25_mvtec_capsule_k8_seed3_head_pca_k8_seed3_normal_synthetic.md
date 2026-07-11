# Run ablation_alpha_0p25_mvtec_capsule_k8_seed3_head_pca_k8_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p25_mvtec_capsule_k8_seed3.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9593810068252008`
- `auroc`: `0.843238930993219`
- `brier`: `0.2057804346180398`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.2964197893937429`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.004293276490925839`
- `max_f1`: `0.9285714285714286`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6040887381332616`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_alpha_0p25_mvtec_capsule_k8_seed3_head_pca_k8_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
