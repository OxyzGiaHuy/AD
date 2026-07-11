# Run ablation_alpha_0p5_mvtec_zipper_k8_seed4_head_pca_k8_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p5_mvtec_zipper_k8_seed4.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9966710110999584`
- `auroc`: `0.989233193277311`
- `brier`: `0.16836522856207134`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.32761103625329124`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0025066127445524103`
- `max_f1`: `0.9875518672199171`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.52498180037894`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_alpha_0p5_mvtec_zipper_k8_seed4_head_pca_k8_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
