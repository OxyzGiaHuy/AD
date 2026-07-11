# Run subspacead_mvtec_capsule_k1_seed4_subspacead_k1_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/subspacead_mvtec_capsule_k1_seed4.yaml`
- Dataset: `mvtec`
- Model: `subspacead`

## Metrics

- `ap`: `0.9606937181678282`
- `auroc`: `0.8496210610291185`
- `brier`: `0.23144170621450916`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.29988952116532763`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.001357729970054193`
- `max_f1`: `0.9308755760368663`
- `model_storage_mb`: `0.09521484375`
- `nll`: `0.65598429215295`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/subspacead_mvtec_capsule_k1_seed4_subspacead_k1_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
