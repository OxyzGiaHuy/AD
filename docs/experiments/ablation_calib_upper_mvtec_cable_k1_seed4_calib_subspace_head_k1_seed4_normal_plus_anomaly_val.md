# Run ablation_calib_upper_mvtec_cable_k1_seed4_calib_subspace_head_k1_seed4_normal_plus_anomaly_val

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_calib_upper_mvtec_cable_k1_seed4.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9287049192686738`
- `auroc`: `0.8712089738263399`
- `brier`: `0.3564403052613271`
- `calibration_anomaly_val_count`: `9`
- `ece`: `0.37040589210834907`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.00246976467893056`
- `max_f1`: `0.8518518518518519`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `1.202253245570882`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_calib_upper_mvtec_cable_k1_seed4_calib_subspace_head_k1_seed4_normal_plus_anomaly_val/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
