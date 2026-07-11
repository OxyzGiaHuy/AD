# Run subspacead_mvtec_grid_k1_seed4_subspacead_k1_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/subspacead_mvtec_grid_k1_seed4.yaml`
- Dataset: `mvtec`
- Model: `subspacead`

## Metrics

- `ap`: `0.9949224602742585`
- `auroc`: `0.985797827903091`
- `brier`: `0.19881735649022794`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.35465389337295145`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0013579057816129464`
- `max_f1`: `0.9655172413793104`
- `model_storage_mb`: `0.09521484375`
- `nll`: `0.5886654207019685`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/subspacead_mvtec_grid_k1_seed4_subspacead_k1_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
