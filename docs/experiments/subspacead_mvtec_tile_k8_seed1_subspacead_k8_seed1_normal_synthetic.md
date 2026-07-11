# Run subspacead_mvtec_tile_k8_seed1_subspacead_k8_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/subspacead_mvtec_tile_k8_seed1.yaml`
- Dataset: `mvtec`
- Model: `subspacead`

## Metrics

- `ap`: `0.9898483790983981`
- `auroc`: `0.9758297258297258`
- `brier`: `0.2544248685374047`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.26694082042090916`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0013041807832116755`
- `max_f1`: `0.9585798816568047`
- `model_storage_mb`: `0.09521484375`
- `nll`: `1.0380063283895686`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/subspacead_mvtec_tile_k8_seed1_subspacead_k8_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
