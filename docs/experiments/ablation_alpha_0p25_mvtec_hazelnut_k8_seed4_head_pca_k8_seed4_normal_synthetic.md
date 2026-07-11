# Run ablation_alpha_0p25_mvtec_hazelnut_k8_seed4_head_pca_k8_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p25_mvtec_hazelnut_k8_seed4.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9882778432681079`
- `auroc`: `0.9775`
- `brier`: `0.22540352816140263`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.16694657098163257`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0035855241119861605`
- `max_f1`: `0.971830985915493`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.643545312609726`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_alpha_0p25_mvtec_hazelnut_k8_seed4_head_pca_k8_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
