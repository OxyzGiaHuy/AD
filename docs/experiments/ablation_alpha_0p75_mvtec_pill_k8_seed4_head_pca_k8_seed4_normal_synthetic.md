# Run ablation_alpha_0p75_mvtec_pill_k8_seed4_head_pca_k8_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p75_mvtec_pill_k8_seed4.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9817530218562533`
- `auroc`: `0.9173486088379705`
- `brier`: `0.14706030408747595`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.2719381287426292`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0021955040534456334`
- `max_f1`: `0.9444444444444444`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.4775310636114256`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_alpha_0p75_mvtec_pill_k8_seed4_head_pca_k8_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
