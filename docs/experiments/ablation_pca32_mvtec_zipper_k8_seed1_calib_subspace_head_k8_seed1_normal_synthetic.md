# Run ablation_pca32_mvtec_zipper_k8_seed1_calib_subspace_head_k8_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca32_mvtec_zipper_k8_seed1.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9831105495311214`
- `auroc`: `0.9411764705882353`
- `brier`: `0.1025548030959695`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.11733376518483979`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0014121364308706183`
- `max_f1`: `0.9477911646586346`
- `model_storage_mb`: `0.4253120422363281`
- `nll`: `0.36898244184952833`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_pca32_mvtec_zipper_k8_seed1_calib_subspace_head_k8_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
