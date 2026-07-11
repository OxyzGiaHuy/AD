# Run ablation_pca16_mvtec_pill_k8_seed1_calib_subspace_head_k8_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca16_mvtec_pill_k8_seed1.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9647179682996061`
- `auroc`: `0.8488816148390617`
- `brier`: `0.07753367460456553`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.06646600963469756`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.002667018842554378`
- `max_f1`: `0.9459459459459459`
- `model_storage_mb`: `0.4018745422363281`
- `nll`: `0.27935240733059924`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_pca16_mvtec_pill_k8_seed1_calib_subspace_head_k8_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
