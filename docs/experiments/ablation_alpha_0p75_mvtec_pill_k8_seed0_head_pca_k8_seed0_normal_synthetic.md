# Run ablation_alpha_0p75_mvtec_pill_k8_seed0_head_pca_k8_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p75_mvtec_pill_k8_seed0.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9847305248811156`
- `auroc`: `0.924986361156574`
- `brier`: `0.13726370319885023`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.17131283968508598`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.002725535881019638`
- `max_f1`: `0.9403508771929825`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.45308174598634154`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_alpha_0p75_mvtec_pill_k8_seed0_head_pca_k8_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
