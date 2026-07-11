# Run ablation_alpha_0p0_mvtec_zipper_k8_seed3_head_pca_k8_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p0_mvtec_zipper_k8_seed3.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.986160566897843`
- `auroc`: `0.9495798319327731`
- `brier`: `0.23196339394895732`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.38519628158468283`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0025032027100293053`
- `max_f1`: `0.9444444444444444`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6569861413151364`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_alpha_0p0_mvtec_zipper_k8_seed3_head_pca_k8_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
