# Run ablation_alpha_1p0_mvtec_hazelnut_k8_seed4_head_pca_k8_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_1p0_mvtec_hazelnut_k8_seed4.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9271836862832503`
- `auroc`: `0.8671428571428571`
- `brier`: `0.24359030479835111`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.12727511362596`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0027721268209544097`
- `max_f1`: `0.8489208633093526`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6855862605762493`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_alpha_1p0_mvtec_hazelnut_k8_seed4_head_pca_k8_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
