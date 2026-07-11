# Run ablation_alpha_0p75_mvtec_pill_k1_seed1_head_pca_k1_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p75_mvtec_pill_k1_seed1.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9767924819435346`
- `auroc`: `0.8914348063284233`
- `brier`: `0.15764196900642152`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.21180305295361726`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0021763576785782854`
- `max_f1`: `0.9379310344827586`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.5012289026629128`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_alpha_0p75_mvtec_pill_k1_seed1_head_pca_k1_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
