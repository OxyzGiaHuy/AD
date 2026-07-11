# Run ablation_pca16_mvtec_pill_k8_seed4_calib_subspace_head_k8_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca16_mvtec_pill_k8_seed4.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9750246419965067`
- `auroc`: `0.8764320785597381`
- `brier`: `0.07744893971584967`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.06094406355551616`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.001518804959194389`
- `max_f1`: `0.9427609427609428`
- `model_storage_mb`: `0.4018745422363281`
- `nll`: `0.2522172823625007`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_pca16_mvtec_pill_k8_seed4_calib_subspace_head_k8_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
