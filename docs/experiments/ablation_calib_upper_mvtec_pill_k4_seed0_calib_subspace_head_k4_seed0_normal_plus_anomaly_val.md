# Run ablation_calib_upper_mvtec_pill_k4_seed0_calib_subspace_head_k4_seed0_normal_plus_anomaly_val

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_calib_upper_mvtec_pill_k4_seed0.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9895219218751542`
- `auroc`: `0.9533615990308903`
- `brier`: `0.0778962381994002`
- `calibration_anomaly_val_count`: `14`
- `ece`: `0.07171413078417188`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.002091235815991763`
- `max_f1`: `0.9565217391304348`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `0.24506082915393768`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_calib_upper_mvtec_pill_k4_seed0_calib_subspace_head_k4_seed0_normal_plus_anomaly_val/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
