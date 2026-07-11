# Run ablation_pca32_mvtec_screw_k8_seed4_calib_subspace_head_k8_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca32_mvtec_screw_k8_seed4.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.8493135384227993`
- `auroc`: `0.6409100225456036`
- `brier`: `0.23793819771238325`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.2298948839481454`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0020307788159698247`
- `max_f1`: `0.8530465949820788`
- `model_storage_mb`: `0.4253120422363281`
- `nll`: `0.8668161021350322`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_pca32_mvtec_screw_k8_seed4_calib_subspace_head_k8_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
