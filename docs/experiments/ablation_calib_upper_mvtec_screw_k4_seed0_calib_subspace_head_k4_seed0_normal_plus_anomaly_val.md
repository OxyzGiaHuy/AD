# Run ablation_calib_upper_mvtec_screw_k4_seed0_calib_subspace_head_k4_seed0_normal_plus_anomaly_val

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_calib_upper_mvtec_screw_k4_seed0.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.8663238908549645`
- `auroc`: `0.7479674796747967`
- `brier`: `0.17921773305818814`
- `calibration_anomaly_val_count`: `11`
- `ece`: `0.18158842608232628`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.002111554045805195`
- `max_f1`: `0.8806584362139918`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `0.7465693935579334`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_calib_upper_mvtec_screw_k4_seed0_calib_subspace_head_k4_seed0_normal_plus_anomaly_val/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
