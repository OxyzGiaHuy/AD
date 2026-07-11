# Run ablation_pca128_mvtec_cable_k1_seed4_calib_subspace_head_k1_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca128_mvtec_cable_k1_seed4.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9240475162891859`
- `auroc`: `0.8600074962518741`
- `brier`: `0.3864844838108496`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.38654967625935877`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0023703096807003022`
- `max_f1`: `0.8379888268156425`
- `model_storage_mb`: `0.5659370422363281`
- `nll`: `3.76474109874818`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_pca128_mvtec_cable_k1_seed4_calib_subspace_head_k1_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
