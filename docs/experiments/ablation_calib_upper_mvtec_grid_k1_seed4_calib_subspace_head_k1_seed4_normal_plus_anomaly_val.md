# Run ablation_calib_upper_mvtec_grid_k1_seed4_calib_subspace_head_k1_seed4_normal_plus_anomaly_val

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_calib_upper_mvtec_grid_k1_seed4.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9939154910674972`
- `auroc`: `0.9844322344322345`
- `brier`: `0.15061325545220833`
- `calibration_anomaly_val_count`: `5`
- `ece`: `0.1851050600613633`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.005198543967857753`
- `max_f1`: `0.9622641509433962`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `0.4424689463200671`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_calib_upper_mvtec_grid_k1_seed4_calib_subspace_head_k1_seed4_normal_plus_anomaly_val/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
