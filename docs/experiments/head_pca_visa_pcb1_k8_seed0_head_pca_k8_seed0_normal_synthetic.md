# Run head_pca_visa_pcb1_k8_seed0_head_pca_k8_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/visa_full/head_pca_visa_pcb1_k8_seed0.yaml`
- Dataset: `visa`
- Model: `head_pca`

## Metrics

- `ap`: `0.8751003849521737`
- `auroc`: `0.8863`
- `brier`: `0.24391241882808654`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.23984633818268775`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.004790130695328116`
- `max_f1`: `0.8333333333333334`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6809288460268226`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/head_pca_visa_pcb1_k8_seed0_head_pca_k8_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
