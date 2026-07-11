# Run subspacead_mvtec_screw_k8_seed0_subspacead_k8_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/subspacead_mvtec_screw_k8_seed0.yaml`
- Dataset: `mvtec`
- Model: `subspacead`

## Metrics

- `ap`: `0.9080342957271241`
- `auroc`: `0.8239393318302931`
- `brier`: `0.6561615400177414`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.679654981661588`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0013795477803796529`
- `max_f1`: `0.9007633587786259`
- `model_storage_mb`: `0.09521484375`
- `nll`: `2.0963696510928225`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/subspacead_mvtec_screw_k8_seed0_subspacead_k8_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
