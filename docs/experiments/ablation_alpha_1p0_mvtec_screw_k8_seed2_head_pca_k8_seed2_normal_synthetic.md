# Run ablation_alpha_1p0_mvtec_screw_k8_seed2_head_pca_k8_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_1p0_mvtec_screw_k8_seed2.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.880660221217994`
- `auroc`: `0.7343717974994876`
- `brier`: `0.18291751548226892`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.07295683883130556`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0017092159832827747`
- `max_f1`: `0.8560606060606061`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.5495566910050077`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_alpha_1p0_mvtec_screw_k8_seed2_head_pca_k8_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
