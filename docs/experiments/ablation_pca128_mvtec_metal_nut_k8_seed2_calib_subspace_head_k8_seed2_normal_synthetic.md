# Run ablation_pca128_mvtec_metal_nut_k8_seed2_calib_subspace_head_k8_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca128_mvtec_metal_nut_k8_seed2.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9967475042016317`
- `auroc`: `0.9863147605083089`
- `brier`: `0.08954617370675422`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.10428785265463854`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.002141827814604925`
- `max_f1`: `0.972972972972973`
- `model_storage_mb`: `0.5659370422363281`
- `nll`: `0.3715572991987476`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_pca128_mvtec_metal_nut_k8_seed2_calib_subspace_head_k8_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
