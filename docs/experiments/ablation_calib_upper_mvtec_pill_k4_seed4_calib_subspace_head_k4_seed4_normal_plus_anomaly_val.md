# Run ablation_calib_upper_mvtec_pill_k4_seed4_calib_subspace_head_k4_seed4_normal_plus_anomaly_val

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_calib_upper_mvtec_pill_k4_seed4.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.983905611644855`
- `auroc`: `0.9327680193821926`
- `brier`: `0.07645652283764362`
- `calibration_anomaly_val_count`: `14`
- `ece`: `0.07509460353773402`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0020423420625769236`
- `max_f1`: `0.9534883720930233`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `0.26542516651421516`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_calib_upper_mvtec_pill_k4_seed4_calib_subspace_head_k4_seed4_normal_plus_anomaly_val/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
