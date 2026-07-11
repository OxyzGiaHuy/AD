# Run head_pca_visa_pcb1_k8_seed4_head_pca_k8_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/visa_full/head_pca_visa_pcb1_k8_seed4.yaml`
- Dataset: `visa`
- Model: `head_pca`

## Metrics

- `ap`: `0.8615425670617582`
- `auroc`: `0.8758`
- `brier`: `0.2431159825299723`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.22024974331259728`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.002216993570327759`
- `max_f1`: `0.8310502283105022`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6793420426169654`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/head_pca_visa_pcb1_k8_seed4_head_pca_k8_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
