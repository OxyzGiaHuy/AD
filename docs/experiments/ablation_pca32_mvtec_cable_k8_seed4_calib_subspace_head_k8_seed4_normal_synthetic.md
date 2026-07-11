# Run ablation_pca32_mvtec_cable_k8_seed4_calib_subspace_head_k8_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca32_mvtec_cable_k8_seed4.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9465022602992833`
- `auroc`: `0.8946776611694153`
- `brier`: `0.21682124807035644`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.24183364652097222`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.002457141342262427`
- `max_f1`: `0.872093023255814`
- `model_storage_mb`: `0.4253120422363281`
- `nll`: `0.6721394068122574`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_pca32_mvtec_cable_k8_seed4_calib_subspace_head_k8_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
