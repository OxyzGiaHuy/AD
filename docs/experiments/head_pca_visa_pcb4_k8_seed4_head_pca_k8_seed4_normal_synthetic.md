# Run head_pca_visa_pcb4_k8_seed4_head_pca_k8_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/visa_full/head_pca_visa_pcb4_k8_seed4.yaml`
- Dataset: `visa`
- Model: `head_pca`

## Metrics

- `ap`: `0.9180195851780804`
- `auroc`: `0.9245544554455446`
- `brier`: `0.23993090290936583`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.031324695740173096`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.013530512910280654`
- `max_f1`: `0.8818181818181818`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6729968203191213`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/head_pca_visa_pcb4_k8_seed4_head_pca_k8_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
