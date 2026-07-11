# Run ablation_pca32_mvtec_screw_k4_seed4_calib_subspace_head_k4_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca32_mvtec_screw_k4_seed4.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.8127374188525036`
- `auroc`: `0.6234884197581472`
- `brier`: `0.22831550900362413`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.22584270182996982`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.00245114624267444`
- `max_f1`: `0.8530465949820788`
- `model_storage_mb`: `0.4253120422363281`
- `nll`: `1.0035024566837705`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_pca32_mvtec_screw_k4_seed4_calib_subspace_head_k4_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
