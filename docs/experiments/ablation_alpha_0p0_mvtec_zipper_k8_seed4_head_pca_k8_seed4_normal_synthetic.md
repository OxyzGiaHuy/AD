# Run ablation_alpha_0p0_mvtec_zipper_k8_seed4_head_pca_k8_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p0_mvtec_zipper_k8_seed4.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9931848610070828`
- `auroc`: `0.9753151260504201`
- `brier`: `0.22965364892584453`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.4002695853347021`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0018797824837711473`
- `max_f1`: `0.9554655870445344`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6523290140942998`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_alpha_0p0_mvtec_zipper_k8_seed4_head_pca_k8_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
