# Run ablation_pca16_mvtec_wood_k8_seed4_calib_subspace_head_k8_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca16_mvtec_wood_k8_seed4.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.990084964652896`
- `auroc`: `0.9692982456140351`
- `brier`: `0.10197373390515976`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.1105890934844796`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0026615118678612044`
- `max_f1`: `0.9586776859504132`
- `model_storage_mb`: `0.4018745422363281`
- `nll`: `0.5877391839145751`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_pca16_mvtec_wood_k8_seed4_calib_subspace_head_k8_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
