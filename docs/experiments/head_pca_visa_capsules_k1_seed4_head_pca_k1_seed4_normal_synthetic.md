# Run head_pca_visa_capsules_k1_seed4_head_pca_k1_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/visa_full/head_pca_visa_capsules_k1_seed4.yaml`
- Dataset: `visa`
- Model: `head_pca`

## Metrics

- `ap`: `0.9765018402772226`
- `auroc`: `0.9571666666666667`
- `brier`: `0.23459102128891277`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.11927718203514817`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.00914822556078434`
- `max_f1`: `0.9246231155778895`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6623021260240195`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/head_pca_visa_capsules_k1_seed4_head_pca_k1_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
