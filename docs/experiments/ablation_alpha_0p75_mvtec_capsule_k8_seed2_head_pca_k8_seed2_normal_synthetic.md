# Run ablation_alpha_0p75_mvtec_capsule_k8_seed2_head_pca_k8_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p75_mvtec_capsule_k8_seed2.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9692255605844435`
- `auroc`: `0.8763462305544475`
- `brier`: `0.15375745604898394`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.22291879852612817`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0028433168137615376`
- `max_f1`: `0.9244444444444444`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.4917039324078234`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_alpha_0p75_mvtec_capsule_k8_seed2_head_pca_k8_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
