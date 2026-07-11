# Run head_pca_visa_pcb1_k1_seed1_head_pca_k1_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/visa_full/head_pca_visa_pcb1_k1_seed1.yaml`
- Dataset: `visa`
- Model: `head_pca`

## Metrics

- `ap`: `0.7267473289277133`
- `auroc`: `0.7542`
- `brier`: `0.24701189809782215`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.013017464429140091`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.004315612446516752`
- `max_f1`: `0.7711864406779662`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6871655633268293`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/head_pca_visa_pcb1_k1_seed1_head_pca_k1_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
