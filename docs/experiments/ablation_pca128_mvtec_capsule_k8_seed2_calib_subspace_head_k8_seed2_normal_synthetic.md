# Run ablation_pca128_mvtec_capsule_k8_seed2_calib_subspace_head_k8_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca128_mvtec_capsule_k8_seed2.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9795587274944196`
- `auroc`: `0.9154367770243319`
- `brier`: `0.08926582619843938`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.09042634920809756`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.001673812187756553`
- `max_f1`: `0.9506726457399103`
- `model_storage_mb`: `0.5659370422363281`
- `nll`: `0.4164438806306077`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_pca128_mvtec_capsule_k8_seed2_calib_subspace_head_k8_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
