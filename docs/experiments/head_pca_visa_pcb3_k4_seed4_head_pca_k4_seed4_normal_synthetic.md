# Run head_pca_visa_pcb3_k4_seed4_head_pca_k4_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/visa_full/head_pca_visa_pcb3_k4_seed4.yaml`
- Dataset: `visa`
- Model: `head_pca`

## Metrics

- `ap`: `0.7568353654209551`
- `auroc`: `0.7543564356435644`
- `brier`: `0.24567950855069712`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.004768602142286527`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.01662370938789192`
- `max_f1`: `0.7345132743362832`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6845024180375052`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/head_pca_visa_pcb3_k4_seed4_head_pca_k4_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
