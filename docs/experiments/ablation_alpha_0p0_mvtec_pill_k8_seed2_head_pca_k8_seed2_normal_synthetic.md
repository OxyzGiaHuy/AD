# Run ablation_alpha_0p0_mvtec_pill_k8_seed2_head_pca_k8_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p0_mvtec_pill_k8_seed2.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9865507953697891`
- `auroc`: `0.9380796508456083`
- `brier`: `0.23633054073800921`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.33599609689798193`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.003676123615956592`
- `max_f1`: `0.9655172413793104`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6657742549737831`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_alpha_0p0_mvtec_pill_k8_seed2_head_pca_k8_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
