# Run subspacead_mvtec_zipper_k8_seed1_subspacead_k8_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/subspacead_mvtec_zipper_k8_seed1.yaml`
- Dataset: `mvtec`
- Model: `subspacead`

## Metrics

- `ap`: `0.9860114712943848`
- `auroc`: `0.9495798319327731`
- `brier`: `0.19726454527181597`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.20281143417421554`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0012956944275770755`
- `max_f1`: `0.9477911646586346`
- `model_storage_mb`: `0.09521484375`
- `nll`: `0.838268380535941`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/subspacead_mvtec_zipper_k8_seed1_subspacead_k8_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
