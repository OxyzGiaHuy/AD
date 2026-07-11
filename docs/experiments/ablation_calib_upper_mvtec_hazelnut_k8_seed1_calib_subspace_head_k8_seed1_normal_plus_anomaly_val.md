# Run ablation_calib_upper_mvtec_hazelnut_k8_seed1_calib_subspace_head_k8_seed1_normal_plus_anomaly_val

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_calib_upper_mvtec_hazelnut_k8_seed1.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9947330933962222`
- `auroc`: `0.9916666666666667`
- `brier`: `0.07905216459320576`
- `calibration_anomaly_val_count`: `7`
- `ece`: `0.1447127318932015`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0037654079858539173`
- `max_f1`: `0.9692307692307692`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `0.2535697353102911`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_calib_upper_mvtec_hazelnut_k8_seed1_calib_subspace_head_k8_seed1_normal_plus_anomaly_val/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
