# Run ablation_pca16_mvtec_wood_k1_seed4_calib_subspace_head_k1_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca16_mvtec_wood_k1_seed4.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9843690854565215`
- `auroc`: `0.9543859649122807`
- `brier`: `0.20616647170757124`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.18276123759112783`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.002938389707403847`
- `max_f1`: `0.95`
- `model_storage_mb`: `0.4018745422363281`
- `nll`: `0.6965160502211922`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_pca16_mvtec_wood_k1_seed4_calib_subspace_head_k1_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
