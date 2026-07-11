# Run ablation_pca16_mvtec_tile_k8_seed1_calib_subspace_head_k8_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca16_mvtec_tile_k8_seed1.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.989109362193276`
- `auroc`: `0.9733044733044733`
- `brier`: `0.09477520355237323`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.12343569940481429`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0047270885676655`
- `max_f1`: `0.96`
- `model_storage_mb`: `0.4018745422363281`
- `nll`: `0.2958615373129905`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_pca16_mvtec_tile_k8_seed1_calib_subspace_head_k8_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
