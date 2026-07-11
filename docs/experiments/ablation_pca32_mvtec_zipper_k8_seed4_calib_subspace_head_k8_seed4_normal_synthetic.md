# Run ablation_pca32_mvtec_zipper_k8_seed4_calib_subspace_head_k8_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca32_mvtec_zipper_k8_seed4.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9906860255202994`
- `auroc`: `0.9661239495798319`
- `brier`: `0.07106636257170294`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.08432014697286863`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0015030756765446126`
- `max_f1`: `0.959349593495935`
- `model_storage_mb`: `0.4253120422363281`
- `nll`: `0.2908276051304532`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_pca32_mvtec_zipper_k8_seed4_calib_subspace_head_k8_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
