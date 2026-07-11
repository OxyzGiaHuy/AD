# Run calib_subspace_head_mvtec_tile_k8_seed4_calib_subspace_head_k8_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/calib_subspace_head_mvtec_tile_k8_seed4.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9903259770088614`
- `auroc`: `0.976911976911977`
- `brier`: `0.08421188065658587`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.09552578866266864`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.001286905577294847`
- `max_f1`: `0.9704142011834319`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `0.43213395643775626`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/calib_subspace_head_mvtec_tile_k8_seed4_calib_subspace_head_k8_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
