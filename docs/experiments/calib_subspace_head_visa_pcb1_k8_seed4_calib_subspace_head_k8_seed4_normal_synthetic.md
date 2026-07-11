# Run calib_subspace_head_visa_pcb1_k8_seed4_calib_subspace_head_k8_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/visa_full/calib_subspace_head_visa_pcb1_k8_seed4.yaml`
- Dataset: `visa`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.8615425670617582`
- `auroc`: `0.8758`
- `brier`: `0.29978212795716996`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.33672715136781334`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.00277009611018002`
- `max_f1`: `0.8310502283105022`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `1.3687845114275559`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/calib_subspace_head_visa_pcb1_k8_seed4_calib_subspace_head_k8_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
