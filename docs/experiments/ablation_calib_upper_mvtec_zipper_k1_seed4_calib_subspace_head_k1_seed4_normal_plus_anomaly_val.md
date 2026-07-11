# Run ablation_calib_upper_mvtec_zipper_k1_seed4_calib_subspace_head_k1_seed4_normal_plus_anomaly_val

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_calib_upper_mvtec_zipper_k1_seed4.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9688097724601861`
- `auroc`: `0.9024884259259259`
- `brier`: `0.1289600158749587`
- `calibration_anomaly_val_count`: `11`
- `ece`: `0.13196747345583776`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.002603868967188256`
- `max_f1`: `0.9344978165938864`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `0.4151926704453145`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_calib_upper_mvtec_zipper_k1_seed4_calib_subspace_head_k1_seed4_normal_plus_anomaly_val/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
