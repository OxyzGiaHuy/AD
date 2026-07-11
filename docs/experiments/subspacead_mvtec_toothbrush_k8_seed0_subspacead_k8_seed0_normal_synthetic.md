# Run subspacead_mvtec_toothbrush_k8_seed0_subspacead_k8_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/subspacead_mvtec_toothbrush_k8_seed0.yaml`
- Dataset: `mvtec`
- Model: `subspacead`

## Metrics

- `ap`: `0.9902702275906299`
- `auroc`: `0.975`
- `brier`: `0.2852319958350867`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.2854629868552798`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.001296665430778549`
- `max_f1`: `0.9523809523809523`
- `model_storage_mb`: `0.09521484375`
- `nll`: `2.220316710318254`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/subspacead_mvtec_toothbrush_k8_seed0_subspacead_k8_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
