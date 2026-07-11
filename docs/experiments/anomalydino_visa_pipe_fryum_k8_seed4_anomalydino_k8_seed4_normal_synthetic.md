# Run anomalydino_visa_pipe_fryum_k8_seed4_anomalydino_k8_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/visa_full/anomalydino_visa_pipe_fryum_k8_seed4.yaml`
- Dataset: `visa`
- Model: `anomalydino`

## Metrics

- `ap`: `0.9918649299236277`
- `auroc`: `0.985`
- `brier`: `0.6060214920962051`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.6430222103744745`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.08845747983704011`
- `max_f1`: `0.9803921568627451`
- `model_storage_mb`: `6.0`
- `nll`: `2.0559040341022`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/anomalydino_visa_pipe_fryum_k8_seed4_anomalydino_k8_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
