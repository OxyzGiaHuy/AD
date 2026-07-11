# Run ablation_pca16_mvtec_metal_nut_k1_seed0_calib_subspace_head_k1_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca16_mvtec_metal_nut_k1_seed0.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9301803266293863`
- `auroc`: `0.7981427174975562`
- `brier`: `0.11583734599563188`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.10866676738293352`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.002984298717068589`
- `max_f1`: `0.9326424870466321`
- `model_storage_mb`: `0.4018745422363281`
- `nll`: `0.7248357656056839`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_pca16_mvtec_metal_nut_k1_seed0_calib_subspace_head_k1_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
