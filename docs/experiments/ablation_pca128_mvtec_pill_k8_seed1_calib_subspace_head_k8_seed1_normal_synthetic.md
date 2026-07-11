# Run ablation_pca128_mvtec_pill_k8_seed1_calib_subspace_head_k8_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca128_mvtec_pill_k8_seed1.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9836438289269509`
- `auroc`: `0.9301691216584833`
- `brier`: `0.06700718450233448`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.0722060648286659`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0017178636378870752`
- `max_f1`: `0.958041958041958`
- `model_storage_mb`: `0.5659370422363281`
- `nll`: `0.307535373121479`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_pca128_mvtec_pill_k8_seed1_calib_subspace_head_k8_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
