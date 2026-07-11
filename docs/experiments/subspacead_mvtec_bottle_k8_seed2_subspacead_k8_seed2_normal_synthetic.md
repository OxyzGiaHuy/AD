# Run subspacead_mvtec_bottle_k8_seed2_subspacead_k8_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/subspacead_mvtec_bottle_k8_seed2.yaml`
- Dataset: `mvtec`
- Model: `subspacead`

## Metrics

- `ap`: `0.9903365514293282`
- `auroc`: `0.9746031746031746`
- `brier`: `0.22643583077428667`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.232455950185477`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0013294724231383886`
- `max_f1`: `0.9767441860465116`
- `model_storage_mb`: `0.09521484375`
- `nll`: `0.9122381299836417`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/subspacead_mvtec_bottle_k8_seed2_subspacead_k8_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
