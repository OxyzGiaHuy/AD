# Run ablation_pca16_mvtec_transistor_k8_seed0_calib_subspace_head_k8_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca16_mvtec_transistor_k8_seed0.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.7306559622765348`
- `auroc`: `0.79625`
- `brier`: `0.2056622191935547`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.20709742911159992`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0014857419580221176`
- `max_f1`: `0.6938775510204082`
- `model_storage_mb`: `0.4018745422363281`
- `nll`: `0.6390419117779362`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_pca16_mvtec_transistor_k8_seed0_calib_subspace_head_k8_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
