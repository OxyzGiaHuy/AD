# Run subspacead_mvtec_grid_k8_seed4_subspacead_k8_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/subspacead_mvtec_grid_k8_seed4.yaml`
- Dataset: `mvtec`
- Model: `subspacead`

## Metrics

- `ap`: `0.999697519661222`
- `auroc`: `0.9991645781119465`
- `brier`: `0.26590130906581055`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.2675276123560393`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0013016202272130893`
- `max_f1`: `0.991304347826087`
- `model_storage_mb`: `0.09521484375`
- `nll`: `1.497628944516586`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/subspacead_mvtec_grid_k8_seed4_subspacead_k8_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
