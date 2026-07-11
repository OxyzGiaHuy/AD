# Run subspacead_mvtec_bottle_k8_seed1_subspacead_k8_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/subspacead_mvtec_bottle_k8_seed1.yaml`
- Dataset: `mvtec`
- Model: `subspacead`

## Metrics

- `ap`: `0.9951440148892859`
- `auroc`: `0.9865079365079366`
- `brier`: `0.21754919077576967`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.2260109530874045`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0013081900191953383`
- `max_f1`: `0.9921259842519685`
- `model_storage_mb`: `0.09521484375`
- `nll`: `0.7641390226583118`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/subspacead_mvtec_bottle_k8_seed1_subspacead_k8_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
