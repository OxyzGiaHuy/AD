# Run head_pca_visa_pcb3_k1_seed4_head_pca_k1_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/visa_full/head_pca_visa_pcb3_k1_seed4.yaml`
- Dataset: `visa`
- Model: `head_pca`

## Metrics

- `ap`: `0.638806521186313`
- `auroc`: `0.6057425742574257`
- `brier`: `0.24863400252914375`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.0006253361998505569`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.008263510925259756`
- `max_f1`: `0.6758620689655173`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6904145963582271`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/head_pca_visa_pcb3_k1_seed4_head_pca_k1_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
