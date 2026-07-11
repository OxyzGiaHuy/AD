# Run ablation_pca128_mvtec_screw_k8_seed1_calib_subspace_head_k8_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca128_mvtec_screw_k8_seed1.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.8977380552873108`
- `auroc`: `0.7852018856323018`
- `brier`: `0.16890892959431122`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.1695952164111077`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0014353036298416556`
- `max_f1`: `0.8830188679245283`
- `model_storage_mb`: `0.5659370422363281`
- `nll`: `0.6908599542079019`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_pca128_mvtec_screw_k8_seed1_calib_subspace_head_k8_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
