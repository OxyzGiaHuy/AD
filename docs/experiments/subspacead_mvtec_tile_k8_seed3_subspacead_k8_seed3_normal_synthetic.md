# Run subspacead_mvtec_tile_k8_seed3_subspacead_k8_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/subspacead_mvtec_tile_k8_seed3.yaml`
- Dataset: `mvtec`
- Model: `subspacead`

## Metrics

- `ap`: `0.9927998982583275`
- `auroc`: `0.9834054834054834`
- `brier`: `0.2540769606420165`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.26686000518309755`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0012847760485278235`
- `max_f1`: `0.9764705882352941`
- `model_storage_mb`: `0.09521484375`
- `nll`: `0.9657424988826254`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/subspacead_mvtec_tile_k8_seed3_subspacead_k8_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
