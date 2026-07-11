# Run ablation_pca16_mvtec_zipper_k8_seed1_calib_subspace_head_k8_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca16_mvtec_zipper_k8_seed1.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9770013814241854`
- `auroc`: `0.9212184873949579`
- `brier`: `0.07764364547563285`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.08127058222766548`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0013749713929283698`
- `max_f1`: `0.944`
- `model_storage_mb`: `0.4018745422363281`
- `nll`: `0.26703964472801167`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_pca16_mvtec_zipper_k8_seed1_calib_subspace_head_k8_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
