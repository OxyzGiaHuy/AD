# Run subspacead_mvtec_tile_k4_seed1_subspacead_k4_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/subspacead_mvtec_tile_k4_seed1.yaml`
- Dataset: `mvtec`
- Model: `subspacead`

## Metrics

- `ap`: `0.9916416013011432`
- `auroc`: `0.9801587301587301`
- `brier`: `0.2661934795735633`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.2735364859939641`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.001291859847230789`
- `max_f1`: `0.9655172413793104`
- `model_storage_mb`: `0.09521484375`
- `nll`: `1.177464692865777`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/subspacead_mvtec_tile_k4_seed1_subspacead_k4_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
