# Run subspacead_mvtec_screw_k8_seed4_subspacead_k8_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/subspacead_mvtec_screw_k8_seed4.yaml`
- Dataset: `mvtec`
- Model: `subspacead`

## Metrics

- `ap`: `0.907943548884308`
- `auroc`: `0.8001639680262349`
- `brier`: `0.25582427263842195`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.2558367647230625`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.001356672018300742`
- `max_f1`: `0.8812260536398467`
- `model_storage_mb`: `0.09521484375`
- `nll`: `1.9394753958669562`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/subspacead_mvtec_screw_k8_seed4_subspacead_k8_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
