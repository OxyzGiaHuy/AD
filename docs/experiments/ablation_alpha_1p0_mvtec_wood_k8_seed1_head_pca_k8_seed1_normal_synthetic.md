# Run ablation_alpha_1p0_mvtec_wood_k8_seed1_head_pca_k8_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_1p0_mvtec_wood_k8_seed1.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9875362196175129`
- `auroc`: `0.968421052631579`
- `brier`: `0.17378734026045148`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.03860084240949612`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.00446245736807962`
- `max_f1`: `0.967741935483871`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.5287588907877767`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_alpha_1p0_mvtec_wood_k8_seed1_head_pca_k8_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
