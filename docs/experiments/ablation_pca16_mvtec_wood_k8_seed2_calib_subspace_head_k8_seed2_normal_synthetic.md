# Run ablation_pca16_mvtec_wood_k8_seed2_calib_subspace_head_k8_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca16_mvtec_wood_k8_seed2.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9801916449915915`
- `auroc`: `0.9394736842105263`
- `brier`: `0.1385393060993228`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.15944056267130985`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0013873054398388803`
- `max_f1`: `0.944`
- `model_storage_mb`: `0.4018745422363281`
- `nll`: `0.6281387723845978`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_pca16_mvtec_wood_k8_seed2_calib_subspace_head_k8_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
