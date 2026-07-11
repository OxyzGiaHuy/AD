# Run ablation_pca64_mvtec_hazelnut_k8_seed4_calib_subspace_head_k8_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca64_mvtec_hazelnut_k8_seed4.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9947469153378441`
- `auroc`: `0.9921428571428571`
- `brier`: `0.3083542701169281`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.32670018713582644`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.003711282140152021`
- `max_f1`: `0.9929078014184397`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `1.8998826581432848`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_pca64_mvtec_hazelnut_k8_seed4_calib_subspace_head_k8_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
