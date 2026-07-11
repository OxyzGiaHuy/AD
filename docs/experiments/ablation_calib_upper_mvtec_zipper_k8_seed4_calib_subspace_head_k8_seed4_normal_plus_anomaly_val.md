# Run ablation_calib_upper_mvtec_zipper_k8_seed4_calib_subspace_head_k8_seed4_normal_plus_anomaly_val

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_calib_upper_mvtec_zipper_k8_seed4.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9919313237827646`
- `auroc`: `0.9733796296296297`
- `brier`: `0.04811622408259521`
- `calibration_anomaly_val_count`: `11`
- `ece`: `0.06258656680583957`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0013202940779072898`
- `max_f1`: `0.9511111111111111`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `0.16778614141813836`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_calib_upper_mvtec_zipper_k8_seed4_calib_subspace_head_k8_seed4_normal_plus_anomaly_val/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
