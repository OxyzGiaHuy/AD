# Run ablation_pca128_mvtec_screw_k4_seed0_calib_subspace_head_k4_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca128_mvtec_screw_k4_seed0.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.8416255147107878`
- `auroc`: `0.7181799549087928`
- `brier`: `0.16785547400046863`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.17492292455863206`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0028258317383006216`
- `max_f1`: `0.9007633587786259`
- `model_storage_mb`: `0.5659370422363281`
- `nll`: `1.0091073456361506`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_pca128_mvtec_screw_k4_seed0_calib_subspace_head_k4_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
