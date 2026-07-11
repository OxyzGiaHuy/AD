# Run subspacead_mvtec_screw_k8_seed1_subspacead_k8_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/subspacead_mvtec_screw_k8_seed1.yaml`
- Dataset: `mvtec`
- Model: `subspacead`

## Metrics

- `ap`: `0.9048292220013348`
- `auroc`: `0.7981143676982988`
- `brier`: `0.6354087472911323`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.6659001332242042`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0012583514442667365`
- `max_f1`: `0.875968992248062`
- `model_storage_mb`: `0.09521484375`
- `nll`: `1.9300331704186662`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/subspacead_mvtec_screw_k8_seed1_subspacead_k8_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
