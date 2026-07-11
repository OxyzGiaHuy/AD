# Run patchcore_mvtec_zipper_k1_seed2_patchcore_k1_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/patchcore_mvtec_zipper_k1_seed2.yaml`
- Dataset: `mvtec`
- Model: `patchcore`

## Metrics

- `ap`: `0.9946414631595542`
- `auroc`: `0.9810924369747899`
- `brier`: `0.2119205298013245`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.21192052980132448`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.004872617675669935`
- `max_f1`: `0.9747899159663865`
- `model_storage_mb`: `2.00537109375`
- `nll`: `3.9037204293753867`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/patchcore_mvtec_zipper_k1_seed2_patchcore_k1_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
