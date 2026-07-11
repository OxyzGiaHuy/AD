# Run ablation_calib_upper_mvtec_hazelnut_k8_seed0_calib_subspace_head_k8_seed0_normal_plus_anomaly_val

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_calib_upper_mvtec_hazelnut_k8_seed0.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9866149521865665`
- `auroc`: `0.9777777777777777`
- `brier`: `0.14116709346441572`
- `calibration_anomaly_val_count`: `7`
- `ece`: `0.20876478266368795`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.003254319568282192`
- `max_f1`: `0.9508196721311475`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `0.41133308352903847`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_calib_upper_mvtec_hazelnut_k8_seed0_calib_subspace_head_k8_seed0_normal_plus_anomaly_val/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
