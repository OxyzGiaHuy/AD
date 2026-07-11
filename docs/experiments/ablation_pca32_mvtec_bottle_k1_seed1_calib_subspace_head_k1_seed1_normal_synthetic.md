# Run ablation_pca32_mvtec_bottle_k1_seed1_calib_subspace_head_k1_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca32_mvtec_bottle_k1_seed1.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9621365571311551`
- `auroc`: `0.9134920634920635`
- `brier`: `0.2409511959814475`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.24095750142292804`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.002412421628832817`
- `max_f1`: `0.9448818897637795`
- `model_storage_mb`: `0.4253120422363281`
- `nll`: `3.6533375954437193`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_pca32_mvtec_bottle_k1_seed1_calib_subspace_head_k1_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
