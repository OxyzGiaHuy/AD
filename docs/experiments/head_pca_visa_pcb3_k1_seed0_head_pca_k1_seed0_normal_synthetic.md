# Run head_pca_visa_pcb3_k1_seed0_head_pca_k1_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/visa_full/head_pca_visa_pcb3_k1_seed0.yaml`
- Dataset: `visa`
- Model: `head_pca`

## Metrics

- `ap`: `0.7267892935512887`
- `auroc`: `0.7115841584158416`
- `brier`: `0.2472227812709438`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.004215368880561343`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0037596330825072615`
- `max_f1`: `0.694560669456067`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6875912973869628`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/head_pca_visa_pcb3_k1_seed0_head_pca_k1_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
