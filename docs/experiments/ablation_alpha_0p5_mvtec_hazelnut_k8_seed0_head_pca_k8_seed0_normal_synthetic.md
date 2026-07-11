# Run ablation_alpha_0p5_mvtec_hazelnut_k8_seed0_head_pca_k8_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p5_mvtec_hazelnut_k8_seed0.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9888384039296642`
- `auroc`: `0.9775`
- `brier`: `0.22281079821120367`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.13136465603655034`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0022546591745181517`
- `max_f1`: `0.9577464788732394`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6373766429166715`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_alpha_0p5_mvtec_hazelnut_k8_seed0_head_pca_k8_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
