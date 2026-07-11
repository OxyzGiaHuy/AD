# Run head_pca_visa_pcb3_k8_seed0_head_pca_k8_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/visa_full/head_pca_visa_pcb3_k8_seed0.yaml`
- Dataset: `visa`
- Model: `head_pca`

## Metrics

- `ap`: `0.80230535475523`
- `auroc`: `0.7815841584158416`
- `brier`: `0.24493462602016366`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.004979562700091318`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.003211203656757056`
- `max_f1`: `0.7394957983193278`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6830123875817002`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/head_pca_visa_pcb3_k8_seed0_head_pca_k8_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
