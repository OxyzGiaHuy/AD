# Run ablation_pca128_mvtec_metal_nut_k8_seed4_calib_subspace_head_k8_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca128_mvtec_metal_nut_k8_seed4.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9984475484899933`
- `auroc`: `0.9931573802541545`
- `brier`: `0.08052727269284163`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.09457091319820153`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0014901481730782468`
- `max_f1`: `0.9836065573770492`
- `model_storage_mb`: `0.5659370422363281`
- `nll`: `0.30502845953180596`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_pca128_mvtec_metal_nut_k8_seed4_calib_subspace_head_k8_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
