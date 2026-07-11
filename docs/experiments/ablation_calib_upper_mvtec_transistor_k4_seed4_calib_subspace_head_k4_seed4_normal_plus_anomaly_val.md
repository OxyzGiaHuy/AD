# Run ablation_calib_upper_mvtec_transistor_k4_seed4_calib_subspace_head_k4_seed4_normal_plus_anomaly_val

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_calib_upper_mvtec_transistor_k4_seed4.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.8796188169589505`
- `auroc`: `0.9152777777777777`
- `brier`: `0.19540807580046252`
- `calibration_anomaly_val_count`: `4`
- `ece`: `0.2503902347913633`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0026150502768966057`
- `max_f1`: `0.8169014084507042`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `0.591869754543938`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_calib_upper_mvtec_transistor_k4_seed4_calib_subspace_head_k4_seed4_normal_plus_anomaly_val/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
