# Run ablation_alpha_0p75_mvtec_cable_k8_seed4_head_pca_k8_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p75_mvtec_cable_k8_seed4.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9577509875886396`
- `auroc`: `0.9132308845577212`
- `brier`: `0.23482201077585954`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.07115998069445287`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0018729001035292943`
- `max_f1`: `0.8941176470588236`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6616021571259804`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_alpha_0p75_mvtec_cable_k8_seed4_head_pca_k8_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
